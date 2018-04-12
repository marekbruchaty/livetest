import com.intellij.openapi.application.ApplicationManager;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import editor.Highlighter;
import model.coverage.CovFile;
import model.coverage.CovLine;
import model.coverage.CovTest;
import resources.AppConstants;
import resources.CoverageLoader;
import resources.DataStore;
import subproc.PytestExecutor;
import utils.VirtualFileUtils;

import java.io.File;
import java.util.Timer;
import java.util.TimerTask;
import java.util.logging.Level;
import java.util.logging.Logger;

public class TestCoverageThread extends Thread {

    private static final int PERIOD = 3000; // Wait 3 sec. between checks
    private static final Logger logger = Logger.getLogger(VirtualFileUtils.class.getName());
    private DataStore ds = DataStore.getInstance();

    TestCoverageThread() {
        super("TestCoverageThread");
    }

    @Override public void run() {
        super.run();

        whileProjectNotReady();

        TimerTask timerTask = new TimerTask() {

            @Override public void run() {
                if (DataStore.getInstance().delayElapsed() && !ds.getModifiedFiles().isEmpty()) {
                    logger.info("Running coverage task");

                    // Force save all files in project
                    ApplicationManager.getApplication().invokeAndWait(
                        () -> ApplicationManager.getApplication().runWriteAction(
                            () -> FileDocumentManager.getInstance().saveAllDocuments()));

                    for (String fileName : ds.getModifiedFiles()) {
                        if (!PytestExecutor.isFileSyntaxOk(fileName)) {
                            return;
                        }
                    }

                    // Run coverage for the whole project
                    PytestExecutor.runCoverageForWholeProject(
                        DataStore.getInstance().getActiveProject().getBasePath());

                    // Load coverage data to memory
                    CoverageLoader.loadAndSaveCoverageData();

                    for (String fileName : ds.getCovFileNames()) {
                        CovFile covFile = ds.getCovFile(fileName);

                        System.out.println("Source code file: " + fileName);
                        System.out.println("Covered lines: " + covFile.getLineNumbers());

                        for (Integer lineNumber : covFile.getLineNumbers()) {
                            CovLine covLine = covFile.getCovLine(lineNumber);

                            StringBuilder sb = new StringBuilder();
                            sb.append("Covered by:\n");

                            Highlighter.HighlightType hType = Highlighter.HighlightType.PASS;
                            for (String testName : covLine.getTests()) {
                                CovTest covTest = ds.getCovTest(testName);
                                sb.append(covTest.getName()).append(" - ");
                                if (covTest.passing()) {
                                    sb.append("passing\n");
                                } else {
                                    hType = Highlighter.HighlightType.FAIL;
                                    sb.append("failing\n");
                                }
                            }

                            Highlighter.HighlightType finalHType = hType;
                            ApplicationManager.getApplication().invokeAndWait(
                                () -> ApplicationManager.getApplication().runWriteAction(
                                    () -> Highlighter
                                        .addLineHighlight(fileName, lineNumber, finalHType,
                                            sb.toString())));

                        }
                    }

                    // clear coverage file and code modification records from memory
                    ds.resetModifiedFiles();
                    ds.resetCovFiles();
                    ds.resetCovTests();
                }
            }
        };

        Timer timer = new Timer();
        timer.schedule(timerTask, 0, PERIOD);
    }

    private void whileProjectNotReady() {
        while (ds.getActiveProject() == null) {
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
