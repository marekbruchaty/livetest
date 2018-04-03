package model;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class CoverageMapping {

    @SerializedName("file_name") private String fileName;
    @SerializedName("covered_lines") private List<Integer> coveredLines;

    public CoverageMapping(String filename, List<Integer> coveredLines) {
        this.fileName = filename;
        this.coveredLines = coveredLines;
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public List<Integer> getCoveredLines() {
        return coveredLines;
    }

    public void setCoveredLines(List<Integer> coveredLines) {
        this.coveredLines = coveredLines;
    }
}
