package subproc;

import enums.LivetestErrorCode;
import exceptions.LivetestException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class PytestExecutor {

    private static final String EOL = "\n";

    private PytestExecutor() {
    }

    private static final Logger LOGGER = Logger.getLogger(PytestExecutor.class.getName());

    /**
     * Executes all projects test cases
     *
     * @param projectFilePath projects root path
     */
    public static String runCoverageForWholeProject(String projectFilePath) {
        Process process = execProcess("pytest -v " + projectFilePath  + " --tb=no");
        return getStdInput(process) + EOL + getStdError(process);
    }

    /**
     * Executes test code coverage for specific test case
     *
     * @param testFilePath format -> test file
     * @param testCaseName format -> test case name
     */
    public static String runCoverageForTestCase(String testFilePath, String testCaseName) {
        String command = "pytest -v " + testFilePath + "::" + testCaseName  + " --tb=no";

        LOGGER.log(Level.INFO, "Test case re-run. Executing command: {0}", command);

        Process process = execProcess(command);
        return getStdInput(process) + EOL + getStdError(process);
    }

    public static boolean isFileSyntaxOk(String filePath) {
        try {
            Process p = Runtime.getRuntime().exec("python -m py_compile "  + filePath);
            Scanner scannerError = new Scanner(p.getErrorStream()).useDelimiter("\\A");

            if (scannerError.hasNext()) {
                String resultError = scannerError.hasNext() ? scannerError.next() : null;
                return resultError == null;
            }
            return true;

        } catch (IOException e) {
            return false;
        }
    }

    private static Process execProcess(String command) {
        Process process;
        try {
            process = Runtime.getRuntime().exec(command);
        } catch (IOException e) {
            e.printStackTrace();
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
        return stdInput.lines().collect(Collectors.joining(EOL));
    }

    private static String getStdError(Process process) {
        BufferedReader stdError =
            new BufferedReader(new InputStreamReader(process.getErrorStream()));
        return stdError.lines().collect(Collectors.joining(EOL));

    }

}
