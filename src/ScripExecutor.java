import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;

public class ScripExecutor {

    public boolean checkDependencies() {
        Process process = execProcess("pytest -h\n");
        return process != null && checkOutputForErrors(process);
    }

    public void runCoverage(String filePath) {
        Process process = execProcess("pytest " + filePath);
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
