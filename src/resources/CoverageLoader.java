package resources;

import com.google.gson.Gson;
import enums.LivetestErrorCode;
import exceptions.LivetestException;
import model.CoverageMapping;
import model.TestCaseCoverage;
import model.coverage.CovFile;
import model.coverage.CovLine;
import model.coverage.CovTest;
import utils.FileUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class CoverageLoader {

    private CoverageLoader() {
    }

    public static void loadAndSaveCoverageData(Map<String, String> testMap) {
        saveCoverageToDataStore(loadCoverageData(), testMap);
    }

    private static List<TestCaseCoverage> loadCoverageData() {
        List<String> lines;
        try {
            lines = FileUtils.readLines(
                DataStore.getInstance().getActiveProject().getBasePath() + "/"
                    + AppConstants.COVERAGE_FILE_NAME);
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

    private static void saveCoverageToDataStore(List<TestCaseCoverage> coverages,
        Map<String, String> testMap) {
        DataStore ds = DataStore.getInstance();
        for (TestCaseCoverage coverage : coverages) {
            String testName = coverage.getTestName();

            if (!ds.existsCovTest(testName)) {
                ds.addCovTest(new CovTest(testName));
            }

            CovTest covTest = ds.getCovTest(testName);
            covTest.setPassing(true);
            covTest.setFilePath(testMap.get(testName));

            for (CoverageMapping coverageMapping : coverage.getCoverageMappings()) {
                String fileName = coverageMapping.getFileName();
                List<Integer> coveredLines = coverageMapping.getCoveredLines();

                if (!ds.existsCovFile(fileName)) {
                    ds.putCovFile(new CovFile(fileName));
                }

                CovFile covFile = ds.getCovFile(fileName);

                for (Integer lineNumber : coveredLines) {

                    if (!covFile.existsCovLine(lineNumber)) {
                        covFile.addCovLine(new CovLine(lineNumber));
                    }

                    CovLine covLine = covFile.getCovLine(lineNumber);
                    covLine.addTest(testName);
                }
            }
        }
    }

}
