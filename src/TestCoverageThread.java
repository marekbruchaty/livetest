import com.intellij.openapi.application.ApplicationManager;
import com.intellij.openapi.editor.Document;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import com.intellij.openapi.vfs.LocalFileSystem;
import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.psi.PsiDocumentManager;
import com.intellij.psi.PsiFile;
import editor.Highlighter;
import model.CoverageMapping;
import model.TestCaseCoverage;
import resources.AppConstants;
import resources.CoverageLoader;
import resources.DataStore;
import subproc.PytestExecutor;
import utils.VirtualFileUtils;

import javax.xml.crypto.Data;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.List;
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
                    logger.info("Running coverage task");

                    // Force save all files in project
                    ApplicationManager.getApplication().invokeAndWait(
                        () -> ApplicationManager.getApplication().runWriteAction(
                            () -> FileDocumentManager.getInstance().saveAllDocuments()));


                    //
                    //                    String filePath = "";
                    //                    VirtualFile virtualFile = LocalFileSystem.getInstance().findFileByPath(filePath);
                    //                    Document document = FileDocumentManager.getInstance().getDocument(virtualFile);
                    //                    PsiFile psiFile =
                    //                        PsiDocumentManager.getInstance(DataStore.getInstance().getActiveProject())
                    //                            .getPsiFile(document);



                    // Run coverage for the whole project
                    PytestExecutor.runCoverageForWholeProject(
                        DataStore.getInstance().getActiveProject().getBasePath());

                    // Load coverage data to memory
                    List<TestCaseCoverage> coverageList = CoverageLoader.loadCoverageData();



                    // Add coverage highlighters to gutter
                    for (TestCaseCoverage coverage : coverageList) {
                        String testName = coverage.getTestName();
                        System.out.println("Test name: " + testName);

                        for (CoverageMapping coverageMap : coverage.getCoverageMappings()) {
                            String fileName = coverageMap.getFileName();
                            List<Integer> coveredLines = coverageMap.getCoveredLines();
                            System.out.println("File name: " + fileName);
                            System.out.println("Covered lines: " + coveredLines);

                            // Cannot interact with the editor from background thread
                            ApplicationManager.getApplication().invokeAndWait(
                                () -> ApplicationManager.getApplication().runWriteAction(
                                    () -> Highlighter.addLineHighlight(fileName, coveredLines,
                                        Highlighter.HighlightType.INFO, false,
                                        "Covered by: " + testName)));
                        }
                    }

                    // clear coverage file and code modification records from memory
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
