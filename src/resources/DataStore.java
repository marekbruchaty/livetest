package resources;

import com.google.common.collect.Sets;
import com.intellij.openapi.project.Project;
import model.ChangedFile;
import model.CoverageMapping;
import model.coverage.CovFile;
import model.coverage.CovTest;

import java.util.*;
import java.util.stream.Collectors;

public class DataStore {

    private static final int TIME_DELAY = 3000;
    private static DataStore ourInstance = new DataStore();

    // Current active project
    private Project activeProject;

    // Last file modified by user
    private ChangedFile lastChangedFile = new ChangedFile();

    // Original file state used for change detection
    private Map<String, HashSet<String>> unmodifiedFiles = new HashMap<>();

    // Modified files used to execute used for test selection
    private Map<String, HashSet<Integer>> modifiedFiles = new HashMap<>();

    // Timestamp of last source code change in editor
    private long lastChangeTimeMillis = 0;

    // Coverage information obtained from pytest
    private List<CoverageMapping> coverageMappings = new ArrayList<>();

    private Map<String, CovFile> covFiles = new HashMap<>();
    private Map<String, CovTest> covTests = new HashMap<>();

    public static synchronized DataStore getInstance() {
        return ourInstance;
    }


    private DataStore() {
    }


    /*
    * Active project
    * */
    public Project getActiveProject() {
        return activeProject;
    }

    public void setActiveProject(Project project) {
        this.activeProject = project;
    }


    /*
    * Last changed file
    * */
    public ChangedFile getLastChangedFile() {
        return lastChangedFile;
    }

    public void setLastChangedFile(ChangedFile lastChangedFile) {
        this.lastChangedFile = lastChangedFile;
    }

    public void initChangedFile() {
        this.lastChangedFile = new ChangedFile();
    }


    /*
    * Unmodified files
    * */
    public Map<String, HashSet<String>> getUnmodifiedFiles() {
        return unmodifiedFiles;
    }

    public void initUnmodifiedFiles() {
        this.unmodifiedFiles = new HashMap<>();
    }

    public boolean unmodifiedFileExists(String path) {
        return this.unmodifiedFiles.containsKey(path);
    }

    public void addUnmodifiedFile(String path, Set<String> text) {
        this.unmodifiedFiles.put(path, (HashSet<String>) text);
    }

//    public void updateUnmodifiedFiles() {
//    }


    /*
    * Modified files
    * */
    public Set<String> getModifiedFiles() {
        return modifiedFiles.keySet();
    }

    public void resetModifiedFiles() {
        this.modifiedFiles = new HashMap<>();
    }

    public void addChangedLine(String filePath, int lineNumber) {
        if (modifiedFiles.containsKey(filePath)) {
            modifiedFiles.get(filePath).add(lineNumber);
        } else {
            modifiedFiles.put(filePath, Sets.newHashSet(lineNumber));
        }
    }

    public Set<Integer> getChangedLines(String fileName) {
        return modifiedFiles.get(fileName);
    }

    public void removeChangedLine(String filePath, int lineNumber) {
        if (modifiedFiles.containsKey(filePath)) {
            modifiedFiles.get(filePath).remove(lineNumber);
            if (modifiedFiles.get(filePath).isEmpty()) {
                modifiedFiles.remove(filePath);
            }
        }
    }


    /*
    * Change timestamp
    * */
    public long getLastChangeTimeMillis() {
        return lastChangeTimeMillis;
    }

    public void setLastChangeTimeMillis(long lastChangeTimeMillis) {
        this.lastChangeTimeMillis = lastChangeTimeMillis;
    }

    public void resetLastChangeTimeMillis() {
        this.lastChangeTimeMillis = System.currentTimeMillis();
    }

    public boolean delayElapsed() {
        return lastChangeTimeMillis + TIME_DELAY > System.currentTimeMillis();
    }


    /*
    * Coverage mapping
    * */
    public List<CoverageMapping> getCoverageMappings() {
        return coverageMappings;
    }

    public void setCoverageMappings(List<CoverageMapping> coverageMappings) {
        this.coverageMappings = coverageMappings;
    }


    /*
    * Source code files with coverage
    * */
    public List<String> getCovFileNames() {
        return covFiles.values().stream().map(CovFile::getName).collect(Collectors.toList());
    }

    public CovFile getCovFile(String fileName) {
        return covFiles.get(fileName);
    }

    public void putCovFile(CovFile covFile) {
        this.covFiles.put(covFile.getName(), covFile);
    }

    public void resetCovFiles() {
        this.covFiles = new HashMap<>();
    }

    public boolean isEmptyCovFiles() {
        return covFiles.isEmpty();
    }

    public boolean existsCovFile(String fileName) {
        return covFiles.containsKey(fileName);
    }


    /*
     * Tests with coverage
     * */
    public CovTest getCovTest(String testName) {
        return covTests.get(testName);
    }

    public void addCovTest(CovTest covTest) {
        this.covTests.put(covTest.getName(), covTest);
    }

    public void resetCovTests() {
        this.covTests = new HashMap<>();
    }

    public boolean isEmptyCovTests() {
        return covTests.isEmpty();
    }

    public boolean existsCovTest(String testName) {
        return covTests.containsKey(testName);
    }

    public Map<String, CovTest> getCovTests() {
        return covTests;
    }
}
