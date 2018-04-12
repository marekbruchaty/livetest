package model.coverage;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class CovFile {
    private String name;
    private HashMap<Integer, CovLine> lines = new HashMap<>();

    public CovFile(String name) {
        this.name = name;
    }

    public boolean existsCovLine(int lineNumber) {
        return lines.containsKey(lineNumber);
    }

    public void addCovLine(CovLine line) {
        lines.put(line.getLineNumber(), line);
    }

    public CovLine getCovLine(Integer lineNumber) {
        return this.lines.get(lineNumber);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Map<Integer, CovLine> getLines() {
        return lines;
    }

    public void setLines(Map<Integer, CovLine> lines) {
        this.lines = (HashMap<Integer, CovLine>) lines;
    }

    public List<Integer> getLineNumbers() {
        return lines.values().stream().map(CovLine::getLineNumber).collect(Collectors.toList());
    }

}
