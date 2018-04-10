import com.intellij.openapi.application.ApplicationInfo;
import com.intellij.openapi.application.ApplicationManager;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import resources.AppConstants;
import resources.DataStore;
import utils.VirtualFileUtils;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Timer;
import java.util.TimerTask;
import java.util.logging.Level;
import java.util.logging.Logger;

public class TestCoverageThread extends Thread {

    private static final int PERIOD = 3000; // Wait 3 sec. between checks
    private static final Logger logger = Logger.getLogger(VirtualFileUtils.class.getName());

    TestCoverageThread() {
        super("TestCoverageThread");
    }

    @Override public void run() {
        super.run();

        whileProjectNotReady();

        TimerTask timerTask = new TimerTask() {

            @Override public void run() {
                if (DataStore.getInstance().delayElapsed() && !DataStore.getInstance()
                    .getModifiedFiles().isEmpty()) {
                    logger.info("executing coverage");
                    PytestExecutor.runCoverageForWholeProject(
                        DataStore.getInstance().getActiveProject().getBasePath());

                    ApplicationManager.getApplication().invokeAndWait(
                        () -> ApplicationManager.getApplication().runWriteAction(
                            () -> FileDocumentManager.getInstance().saveAllDocuments()));

                    clearCoverageFile();
                    DataStore.getInstance().resetModifiedFiles();
                }
            }

            private void clearCoverageFile() {
                File f = new File(AppConstants.COVERAGE_FILE_NAME);
                if (f.exists() && !f.isDirectory()) {
                    try {
                        PrintWriter writer = new PrintWriter(f);
                        writer.print("");
                        writer.close();
                    } catch (FileNotFoundException e) {
                        logger.log(Level.SEVERE, "Coverage file clearance failed. Stack trace: {0}",
                            e.getStackTrace());
                    }
                }
            }

        };

        Timer timer = new Timer();
        timer.schedule(timerTask, 0, PERIOD);
    }

    private void whileProjectNotReady() {
        while (DataStore.getInstance().getActiveProject() == null) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                new TestCoverageThread().start();
                logger.log(Level.SEVERE, "Thread {0} interrupted forcefully. Thread restarted.",
                    Thread.currentThread().getName());
                Thread.currentThread().interrupt();
            }
        }
    }

    @Override public synchronized void start() {
        logger.info(getName() + "Starting. Coverage run set to " + PERIOD / 1000 + "sec period.");
        super.start();
    }

}
