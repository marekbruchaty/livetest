package subproc;

import java.util.Arrays;
import java.util.Map;
import java.util.stream.Collectors;

public class PytestReportProcesor {

    private static final String ERROR = "ERROR";
    private static final String PASSED = "PASSED";
    private static final String DOUBLE_DASH_DELIMITER = "::";
    //TODO determine slash type by actual OS
    private static final String SLASH = "/";
    private static final String STEP_BACK = "..";

    private PytestReportProcesor() {
    }

    public static Map<String, String> getTestNamePathMapping(String report, boolean errorOnly) {
        return Arrays.stream(report.split("\n")).filter(
            x -> (errorOnly && x.contains(ERROR)) || (!errorOnly && (x.contains(PASSED) || x
                .contains(ERROR)))).map(x -> x.split(DOUBLE_DASH_DELIMITER)).collect(Collectors
            .toMap(s -> s[1].split(" ")[0], s -> SLASH + s[0].replace(STEP_BACK + SLASH, "")));
    }
}
