package threads;

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

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class TestCoverageTask {
    private static TestCoverageTask ourInstance = new TestCoverageTask();

    public static TestCoverageTask getInstance() {
        return ourInstance;
    }

    private TestCoverageTask() {
    }

    private static final Logger LOGGER = Logger.getLogger(TestCoverageTask.class.getName());
    private DataStore ds = DataStore.getInstance();
    private boolean initialRun = true;

    public void run() {
        if (initialRun || (ds.delayElapsed() && !ds.getModifiedFiles().isEmpty())) {
            LOGGER.log(Level.INFO, "Running coverage task");

            // Force save all files in project
            safeAllFiles();

            // Continue only if source code syntax is correct
            if (!isSyntaxOk())
                return;

            if (initialRun) {
                // Run initial testing and coverage for whole project
                runTestsWholeProject();
            } else {
                // Run tests for changes covered by tests
                runTestsChangesOnly();
            }

            // Update visible highlighters
            updateHighlights();

            updateCoverageData();

            // clear coverage file and code modification records from memory
            cleanUp();

            initialRun = false;
        } else {
            LOGGER.log(Level.INFO, "No changes. Elapsed time: {0}", ds.delayElapsed());
        }
    }

    private void updateCoverageData() {

    }


    private void runTestsChangesOnly() {
        LOGGER.log(Level.INFO, "Running coverage for changed lines covered by test suite only");
        for (String modFileName : ds.getModifiedFiles()) {
            CovFile covFile = ds.getCovFile(modFileName);

            LOGGER.log(Level.INFO, "File {0} modified. These tests need to be reruned", covFile.getName());

            for (Integer lineNumber : ds.getChangedLines(modFileName)) {
                CovLine covLine = covFile.getCovLine(lineNumber + 1);

                if (covLine == null) {
                    LOGGER.log(Level.INFO, "Line number {0} is not covered by any test.", lineNumber);
                    //TODO We should probably rerun all tests for the modified method here
                    continue;
                }

                for (String testName : covLine.getTests()) {
                    runTestForChanges(testName, ds.getCovTest(testName));
                }
            }
        }
    }

    private void runTestForChanges(String testName, CovTest covTest) {
        String report = PytestExecutor.runCoverageForTestCase(covTest.getFilePath(), testName);
        Map<String, String> map = PytestReportProcesor.getTestNamePathMapping(report, true);

        for (String key : map.keySet()) {
            ds.getCovTest(key).setPassing(false);
        }
    }

    private void runTestsWholeProject() {
        LOGGER.log(Level.INFO, "Running coverage for whole project");
        // Run coverage for the whole project
        String report =
            PytestExecutor.runCoverageForWholeProject(ds.getActiveProject().getBasePath());

        LOGGER.log(Level.INFO, "Acquired pytest report:\n{0}", report);

        Map<String, String> testMap = PytestReportProcesor.getTestNamePathMapping(report, false);

        LOGGER.log(Level.INFO, "Test name / test path - map:\n{0}", report);

        // Load coverage data to memory
        CoverageLoader.loadAndSaveCoverageData(testMap);

        // Update test results - if tests have passed or failed
        updateTestResults(report);
    }

    private void safeAllFiles() {
        LOGGER.log(Level.INFO, "Saving all project files");
        ApplicationManager.getApplication().invokeAndWait(() -> ApplicationManager.getApplication()
            .runWriteAction(() -> FileDocumentManager.getInstance().saveAllDocuments()));
    }

    private boolean isSyntaxOk() {
        LOGGER.log(Level.INFO, "Checking file syntax");
        for (String fileName : ds.getModifiedFiles()) {
            if (!PytestExecutor.isFileSyntaxOk(fileName)) {
                return false;
            }
        }
        return true;
    }

    private void cleanUp() {
        LOGGER.log(Level.INFO, "Cleaning metadata");
        ds.resetModifiedFiles();
    }

    private void updateHighlights() {
        LOGGER.log(Level.INFO, "Updating highlights and gutter icons");
        for (String fileName : ds.getCovFileNames()) {
            CovFile covFile = ds.getCovFile(fileName);

            LOGGER.log(Level.INFO, "Source code file: {0}", fileName);
            LOGGER.log(Level.INFO, "Covered lines: {0}", covFile.getLineNumbers());

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
                ApplicationManager.getApplication().invokeAndWait(() -> ApplicationManager.getApplication()
                    .runWriteAction(
                        () -> Highlighter.addLineHighlight(fileName, lineNumber, finalHType, sb.toString())));
            }
        }
    }

    private void updateTestResults(String report) {
        List<String> collect =
            Arrays.stream(report.split("\n")).filter(x -> x.contains("PASSED") || x.contains("ERROR"))
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
}