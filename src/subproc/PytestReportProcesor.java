package subproc;

import org.jetbrains.annotations.NotNull;

import java.util.Arrays;
import java.util.Map;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collector;
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
        return Arrays.stream(getSplit(report)).filter(getStringPredicate(errorOnly))
            .map(x -> x.split(DOUBLE_DASH_DELIMITER)).collect(getMapCollector());
    }

    public static Map<String, Boolean> getTestNameStatusMapping(String report) {
        return Arrays.stream(getSplit(report)).filter(PytestReportProcesor::isStatus).map(getNameAndStatus())
            .collect(getNameStatusCollector());
    }

    @NotNull private static Collector<String[], ?, Map<String, Boolean>> getNameStatusCollector() {
        return Collectors.toMap(x -> x[0], x -> isPass(x[1]));
    }

    @NotNull private static Function<String, String[]> getNameAndStatus() {
        return x -> x.split(DOUBLE_DASH_DELIMITER)[1].split(" ");
    }

    @NotNull private static String[] getSplit(String report) {
        return report.split("\n");
    }

    @NotNull private static Collector<String[], ?, Map<String, String>> getMapCollector() {
        return Collectors.toMap(s -> s[1].split(" ")[0], s -> SLASH + s[0].replace(STEP_BACK + SLASH, ""));
    }

    @NotNull private static Predicate<String> getStringPredicate(boolean errorOnly) {
        return x -> (errorOnly && isError(x)) || (!errorOnly && (isPass(x) || isError(x)));
    }


    private static boolean isError(String x) {
        return x.contains(ERROR);
    }

    private static boolean isPass(String x) {
        return x.contains(PASSED);
    }

    private static boolean isStatus(String x) {
        return isPass(x) || isError(x);
    }
}
