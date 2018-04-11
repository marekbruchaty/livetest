package subproc;

import enums.LivetestErrorCode;
import exceptions.LivetestException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class PytestExecutor {

    private static final Logger log = Logger.getLogger(PytestExecutor.class.getName());

    public boolean checkDependencies() {
        Process process = execProcess("pytest -h\n");
        return process != null && checkOutputForErrors(process);
    }

    /**
     * Executes all projects test cases
     *
     * @param projectFilePath projects root path
     */
    public static void runCoverageForWholeProject(String projectFilePath) {
        Process process = execProcess("pytest " + projectFilePath);
        String stdInput = getStdInput(process);
        String stdError = getStdError(process);
        System.out.println(stdInput);
        System.out.println(stdError);
    }

    /**
     * Executes test code coverage for specific test case
     *
     * @param testCaseUrl format -> filePath::module::testCase
     */
    public static void runCoverageForTestCase(String testCaseUrl) {
        Process process = execProcess("pytest " + testCaseUrl);

    }

    /**
     * Executes test code coverage for specific test cases
     *
     * @param testCaseUrls format -> filePath::module::testCase
     */
    public static void runCoverageForTests(List<String> testCaseUrls) {
        for (String url : testCaseUrls) {
            Process process = execProcess("pytest ");
        }
    }

    public static boolean checkPythonFileSyntax(String filePath) {
        try {
            execProcess("python -m py_compile " + filePath);
            return true;
        } catch (LivetestException e) {
            log.log(Level.INFO, "File {0} syntax error. Moving on...", filePath);
            return false;
        }
    }

    private static boolean checkOutputForErrors(Process process) {
        InputStream errorStream = process.getErrorStream();
        return new Scanner(errorStream).hasNext();
    }

    private static Process execProcess(String command) {
        Process process;
        try {
            process = Runtime.getRuntime().exec(command);
        } catch (IOException e) {
            process = null;
        }

        if (process == null) {
            throw new LivetestException(
                LivetestErrorCode.ERROR_OCCURRED_WHILE_SUBPROCESS_EXECUTION);
        } else {
            return process;
        }
    }


    private static String getStdInput(Process process) {
        BufferedReader stdInput =
            new BufferedReader(new InputStreamReader(process.getInputStream()));
        return stdInput.lines().collect(Collectors.joining("\n"));
    }

    private static String getStdError(Process process) {
        BufferedReader stdError =
            new BufferedReader(new InputStreamReader(process.getErrorStream()));
        return stdError.lines().collect(Collectors.joining("\n"));

    }

}
