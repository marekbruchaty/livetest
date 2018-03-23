package model;

import org.apache.commons.lang.StringUtils;

public class FileLine {

    public enum Change {
        NON, ADD, DEL
    }

    private int lineNumber;
    private String lineContent;
    private Change lineChange;

    public FileLine(Change lineChange, int lineNumber, String lineContent) {
        this.lineChange = lineChange;
        this.lineNumber = lineNumber;
        this.lineContent = lineContent;
    }

    public int getLineNumber() {
        return lineNumber;
    }

    public String getLineContent() {
        return lineContent;
    }

    public Change getLineChange() {
        return lineChange;
    }

    @Override
    public String toString() {
        String changeSign = " ";
        if (this.lineChange == Change.ADD) {
            changeSign = "+";
        } else if (this.lineChange == Change.DEL) {
            changeSign = "-";
        }
        return String.format("%s%d\t: %s", changeSign, lineNumber, lineContent);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof FileLine) {
            return StringUtils.equals(this.lineContent, ((FileLine) obj).lineContent);
        }
        return super.equals(obj);
    }
}
