package model;

import com.google.gson.annotations.SerializedName;

import java.util.List;

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
}
