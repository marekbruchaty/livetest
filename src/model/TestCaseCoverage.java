package model;

import com.google.gson.annotations.SerializedName;

import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class TestCaseCoverage {

    @SerializedName("test_name") private String testName;
    @SerializedName("coverage_mapping") private List<CoverageMapping> coverageMappings;

    public TestCaseCoverage(String testName, List<CoverageMapping> coverageMapping) {
        this.testName = testName;
        this.coverageMappings = coverageMapping;
    }

    public String getTestName() {
        return testName;
    }

    public void setTestName(String testName) {
        this.testName = testName;
    }

    public List<CoverageMapping> getCoverageMappings() {
        return coverageMappings;
    }

    public void setCoverageMappings(List<CoverageMapping> coverageMappings) {
        this.coverageMappings = coverageMappings;
    }

    public List<Integer> getCoverageForFile(String fileName) {
        Optional<CoverageMapping> result =
            coverageMappings.stream().filter(x -> x.getFileName().equalsIgnoreCase(fileName))
                .findFirst();

        return result.isPresent() ? result.get().getCoveredLines() : Collections.emptyList();
    }
}
