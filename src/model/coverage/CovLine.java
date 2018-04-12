package model.coverage;

import java.util.HashSet;
import java.util.Set;

public class CovLine {
    private int lineNumber;
    private Set<String> tests = new HashSet<>();

    public CovLine(int lineNumber) {
        this.lineNumber = lineNumber;
    }

    public void addTest(String testName) {
        tests.add(testName);
    }

    public int getLineNumber() {
        return lineNumber;
    }

    public void setLineNumber(int lineNumber) {
        this.lineNumber = lineNumber;
    }

    public Set<String> getTests() {
        return tests;
    }
}
