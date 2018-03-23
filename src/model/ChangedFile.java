package model;

import listeners.LivetestProjectManagerListenerImpl;
import org.apache.commons.lang.StringUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Logger;

public class ChangedFile {

    private static final Logger log = Logger.getLogger(LivetestProjectManagerListenerImpl.class.getName());

    private String fileName;
    private String originalContent;
    private String modifiedContent;

    public ChangedFile() {
    }

    public ChangedFile(String fileName) {
        this.fileName = fileName;
    }

    public String getFileName() {
        return fileName;
    }

    public String getOriginalContent() {
        return originalContent;
    }

    public void setOriginalContent(String originalContent) {
        this.originalContent = originalContent;
    }

    public String getModifiedContent() {
        return modifiedContent;
    }

    public void setModifiedContent(String modifiedContent) {
        this.modifiedContent = modifiedContent;
    }

    public void printOrigFile() {
        List<String> lines = Arrays.asList(originalContent.split("\n"));

        for (int i = 0; i < lines.size(); i++) {
            System.out.println(String.format("%s    : %s", i, lines.get(i)));
        }
    }

    public void printModFile() {
        List<String> lines = Arrays.asList(modifiedContent.split("\n"));

        for (int i = 0; i < lines.size(); i++) {
            System.out.println(String.format("%s    : %s", i, lines.get(i)));
        }
    }

    public ArrayList<FileLine> getChangedSequences() {

        List<String> originalLines = Arrays.asList(originalContent.split("\n"));
        List<String> modifiedLines = Arrays.asList(modifiedContent.split("\n"));
        ArrayList<FileLine> originalFileLines = getFileLines(originalContent);
        ArrayList<FileLine> modifiedFileLines = getFileLines(modifiedContent);

        System.out.println("\n\nOriginal file");
        for (FileLine line : originalFileLines) {
            System.out.println(line.toString());
        }

        System.out.println("\n\nModified file");
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

        return diffLines;
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

