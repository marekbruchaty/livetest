package resources;

import com.google.gson.Gson;
import enums.LivetestErrorCode;
import exceptions.LivetestException;
import model.TestCaseCoverage;
import utils.FileUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class CoverageLoader {

    public static List<TestCaseCoverage> loadCoverageData() {
        List<String> lines;
        try {
            lines = FileUtils.readLines(DataStore.getInstance().getActiveProject().getBasePath()
                + "/" + AppConstants.COVERAGE_FILE_NAME);
        } catch (IOException e) {
            throw new LivetestException(LivetestErrorCode.NO_COVERAGE_FILE_AVAILABLE);
        }

        Gson gson = new Gson();
        List<TestCaseCoverage> coverages = new ArrayList<>();

        for (String line : lines) {
            coverages.add(gson.fromJson(line, TestCaseCoverage.class));
        }

        return coverages;
    }

}
