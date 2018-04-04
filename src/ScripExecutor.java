import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.Scanner;

public class ScripExecutor {

    public boolean checkDependencies() {
        Process process = execProcess("pytest -h\n");
        return process != null && checkOutputForErrors(process);
    }

    /**
     * Executes test code coverage for specific test case
     * @param filePath gile path with filename (example: /dir//main.py)
     */
    public void runCoverageForProject(String filePath) {
        Process process = execProcess("pytest " + filePath);
    }

    /**
     * Executes test code coverage for specific test case
     * @param testCaseUrl format -> filePath::module::testCase
     */
    public void runCoverageForTest(String testCaseUrl) {
        Process process = execProcess("pytest " + testCaseUrl);
    }

    /**
     * Executes test code coverage for specific test cases
     * @param testCaseUrls format -> filePath::module::testCase
     */
    public void runCoverageForTests(List<String> testCaseUrls) {
        for (String url : testCaseUrls) {
            Process process = execProcess("pytest ");
        }
    }

    private boolean checkOutputForErrors(Process process) {
        InputStream errorStream = process.getErrorStream();
        return new Scanner(errorStream).hasNext();
    }

    private Process execProcess(String command) {
        Process process;
        try {
            process = Runtime.getRuntime().exec(command);
        } catch (IOException e) {
            return null;
        }
        return process;
    }

}
