package tests;

import org.junit.jupiter.api.Test;
import subproc.PytestExecutor;

class PytestExecutorTest {


    @Test void runCoverageForWholeProject() {
        PytestExecutor.runCoverageForWholeProject("/work/priv/python/python-tests");
    }

}
