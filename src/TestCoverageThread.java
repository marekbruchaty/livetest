import com.intellij.openapi.application.ApplicationManager;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import editor.Highlighter;
import model.coverage.CovFile;
import model.coverage.CovLine;
import model.coverage.CovTest;
import resources.CoverageLoader;
import resources.DataStore;
import subproc.PytestExecutor;
import subproc.PytestReportProcesor;
import utils.VirtualFileUtils;

import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class TestCoverageThread extends Thread {

    private static final int PERIOD = 3000; // Wait 3 sec. between checks
    private static final Logger logger = Logger.getLogger(VirtualFileUtils.class.getName());
    private DataStore ds = DataStore.getInstance();
    private boolean initialRun = true;

    TestCoverageThread() {
        super("TestCoverageThread");
    }

    @Override public void run() {
        super.run();

        // Wait for project to load
        whileProjectNotReady();

        TimerTask timerTask = new TimerTask() {

            @Override public void run() {
                if (initialRun || (DataStore.getInstance().delayElapsed() && !ds.getModifiedFiles()
                    .isEmpty())) {
                    logger.info("Running coverage task");

                    // Force save all files in project
                    safeAllFiles();

                    // Continue only if source code syntax is correct
                    if (!isSyntaxOk())
                        return;

                    // Run tests for changes covered by tests
                    if (!initialRun)
                        runTestsForChanges();

                    // Run initial testing and coverage for whole project
                    if (initialRun)
                        runCoverageForWholeProject();


                    // Update visible highlighters
                    updateHighlights();

                    // clear coverage file and code modification records from memory
                    cleanUp();

                    initialRun = false;
                }
            }

            private void runTestsForChanges() {
                logger.log(Level.INFO, "Running coverage for changed lines covered by test suite");
                for (String modFileName : ds.getModifiedFiles()) {
                    CovFile covFile = ds.getCovFile(modFileName);

                    logger.log(Level.FINEST, "File {0} modified. These tests need to be retested.", covFile.getName());

                    for (Integer lineNumber : ds.getChangedLines(modFileName)) {
                        CovLine covLine = covFile.getCovLine(lineNumber);
                        Set<String> tests = covLine.getTests();

                        for (String testName : tests) {
                            PytestExecutor.runCoverageForTestCase("", testName);
                        }
                    }
                }
            }

            private void runCoverageForWholeProject() {
                logger.log(Level.INFO, "Running coverage for whole project");
                // Run coverage for the whole project
                String report = PytestExecutor.runCoverageForWholeProject(
                    DataStore.getInstance().getActiveProject().getBasePath());

                Map<String, String> testMap =
                    PytestReportProcesor.getTestNamePathMapping(report);

                // Load coverage data to memory
                CoverageLoader.loadAndSaveCoverageData(testMap);

                // Update test results - if tests passed or failed
                updateTestResults(report);
            }

            private void safeAllFiles() {
                logger.log(Level.INFO, "Saving all project files");
                ApplicationManager.getApplication().invokeAndWait(
                    () -> ApplicationManager.getApplication().runWriteAction(
                        () -> FileDocumentManager.getInstance().saveAllDocuments()));
            }

            private boolean isSyntaxOk() {
                logger.log(Level.INFO, "Checking file syntax");
                for (String fileName : ds.getModifiedFiles()) {
                    if (!PytestExecutor.isFileSyntaxOk(fileName)) {
                        return false;
                    }
                }
                return true;
            }

            private void cleanUp() {
                logger.log(Level.INFO, "Cleaning metadata");
                ds.resetModifiedFiles();
            }

            private void updateHighlights() {
                logger.log(Level.INFO, "Updating highlights and gutter icons");
                for (String fileName : ds.getCovFileNames()) {
                    CovFile covFile = ds.getCovFile(fileName);

                    logger.log(Level.FINEST, "Source code file: {0}", fileName);
                    logger.log(Level.FINEST, "Covered lines: {0}", covFile.getLineNumbers());

                    for (Integer lineNumber : covFile.getLineNumbers()) {
                        CovLine covLine = covFile.getCovLine(lineNumber);

                        StringBuilder sb = new StringBuilder();
                        sb.append("Covered by:\n");

                        Highlighter.HighlightType hType = Highlighter.HighlightType.PASS;
                        for (String testName : covLine.getTests()) {
                            CovTest covTest = ds.getCovTest(testName);
                            sb.append(covTest.getName()).append(" - ");
                            if (covTest.isPassing()) {
                                sb.append("passing\n");
                            } else {
                                hType = Highlighter.HighlightType.FAIL;
                                sb.append("failing\n");
                            }
                        }

                        Highlighter.HighlightType finalHType = hType;
                        ApplicationManager.getApplication().invokeAndWait(
                            () -> ApplicationManager.getApplication().runWriteAction(
                                () -> Highlighter.addLineHighlight(fileName, lineNumber, finalHType,
                                    sb.toString())));

                    }
                }
            }

            private void updateTestResults(String results) {
                List<String> collect = Arrays.stream(results.split("\n"))
                    .filter(x -> x.contains("PASSED") || x.contains("ERROR"))
                    .collect(Collectors.toList());
                for (String s : collect) {
                    String[] split = s.split("::")[1].split(" ");
                    String testName = split[0];
                    boolean testPasses = split[1].equalsIgnoreCase("PASSED");
                    if (ds.existsCovTest(testName)) {
                        ds.getCovTest(testName).setPassing(testPasses);
                    }
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
