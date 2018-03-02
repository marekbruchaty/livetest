package model;

import listeners.LivetestProjectManagerListenerImpl;
import org.apache.commons.lang.StringUtils;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Logger;

public class ChangedFile {

    private static final Logger log = Logger.getLogger(LivetestProjectManagerListenerImpl.class.getName());

    private String fileName;
    private String originalCharSequence;
    private String modifiedCharSequence;

    public ChangedFile() {
    }

    public ChangedFile(String fileName) {
        this.fileName = fileName;
    }

    public String getFileName() {
        return fileName;
    }

    public String getOriginalCharSequence() {
        return originalCharSequence;
    }

    public void setOriginalCharSequence(String originalCharSequence) {
        this.originalCharSequence = originalCharSequence;
    }

    public String getModifiedCharSequence() {
        return modifiedCharSequence;
    }

    public void setModifiedCharSequence(String modifiedCharSequence) {
        this.modifiedCharSequence = modifiedCharSequence;
    }

    public void printOrigFile() {
        List<String> lines = Arrays.asList(originalCharSequence.split("\n"));

        for (int i = 0; i < lines.size(); i++) {
            System.out.println(String.format("%s    : %s", i, lines.get(i)));
        }
    }

    public void printModFile() {
        List<String> lines = Arrays.asList(modifiedCharSequence.split("\n"));

        for (int i = 0; i < lines.size(); i++) {
            System.out.println(String.format("%s    : %s", i, lines.get(i)));
        }
    }

    public void getChangedSequences() {

        List<String> originalLines = Arrays.asList(originalCharSequence.split("\n"));
        List<String> modifiedLines = Arrays.asList(modifiedCharSequence.split("\n"));
        ArrayList<FileLine> originalFileLines = getFileLines(originalCharSequence);
        ArrayList<FileLine> modifiedFileLines = getFileLines(modifiedCharSequence);

        for (FileLine line : originalFileLines) {
            System.out.println(line.toString());
        }

        for (FileLine line : modifiedFileLines) {
            System.out.println(line.toString());
        }

        ArrayList<FileLine> diffLines = new ArrayList<>();
        for (FileLine line: originalFileLines) {
            if (!modifiedLines.contains(line.getLineContent())) {
                diffLines.add(new FileLine(FileLine.Change.DEL, line.getLineNumber(), line.getLineContent()));
            }
        }

        for (FileLine line: modifiedFileLines) {
            if (!originalLines.contains(line.getLineContent())) {
                diffLines.add(new FileLine(FileLine.Change.ADD, line.getLineNumber(), line.getLineContent()));
            }
        }

        for (FileLine line: diffLines) {
            System.out.println(line.toString());
        }
    }

    private ArrayList<FileLine> getFileLines(String fileContent) {
        int lineNumber = 1;
        ArrayList<FileLine> fileLines = new ArrayList<>();
        for (String lineContent : fileContent.split("\n"))
            fileLines.add(new FileLine(FileLine.Change.NON, lineNumber++, lineContent));
        return fileLines;
    }

    private static List<FileLine> diffFiles(final List<FileLine> first, final List<FileLine> second) {
        final List<FileLine> diff = new ArrayList<>();
        for (final FileLine fileLine: first) {
            if (!second.contains(fileLine)) {
                diff.add(fileLine);
            }
        }
        return diff;
    }
}

class FileLine {

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