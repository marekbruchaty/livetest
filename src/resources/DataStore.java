package resources;

import com.google.common.collect.Sets;
import com.intellij.openapi.project.Project;
import model.ChangedFile;
import model.CoverageMapping;

import java.util.*;

public class DataStore {

    private static final int TIME_DELAY = 3000;
    private static DataStore ourInstance = new DataStore();

    // Current active project
    private Project activeProject;

    // Last file modified by user
    private ChangedFile lastChangedFile = new ChangedFile();

    // Original file state used for change detection
    private Map<String, List<String>> unmodifiedFiles = new HashMap<>();

    // Modified files used to execute used for test selection
    private Map<String, HashSet<Integer>> modifiedFiles = new HashMap<>();

    // Timestamp of last source code change in editor
    private long lastChangeTimeMillis = 0;

    // Coverage information obtained from pytest
    private List<CoverageMapping> coverageMappings = new ArrayList<>();

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
    public Map<String, List<String>> getUnmodifiedFiles() {
        return unmodifiedFiles;
    }

    public void initUnmodifiedFiles() {
        this.unmodifiedFiles = new HashMap<>();
    }

    public boolean unmodifiedFileExists(String path) {
        return this.unmodifiedFiles.containsKey(path);
    }

    public void addUnmodifiedFile(String path, List<String> text) {
        this.unmodifiedFiles.put(path, text);
    }


    /*
    * Modified files
    * */
    public Map<String, HashSet<Integer>> getModifiedFiles() {
        return modifiedFiles;
    }

    public Map<String, HashSet<Integer>> resetModifiedFiles() {
        return modifiedFiles = new HashMap<>();
    }

    public void addChangedLine(String filePath, int lineNumber) {
        if (modifiedFiles.containsKey(filePath)) {
            modifiedFiles.get(filePath).add(lineNumber);
        } else {
            modifiedFiles.put(filePath, Sets.newHashSet(lineNumber));
        }
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
        return System.currentTimeMillis() + TIME_DELAY > lastChangeTimeMillis;
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
}
