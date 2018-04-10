package resources;

import com.google.common.collect.Sets;
import com.intellij.openapi.project.Project;
import model.ChangedFile;
import model.CoverageMapping;

import java.util.*;

public class DataStore {

  public static final int TIME_DELAY = 3000;
  private static DataStore ourInstance = new DataStore();

  private Project activeProject;
  private ChangedFile lastChangedFile = new ChangedFile();

  private Map<String, List<String>> unmodifiedFiles = new HashMap<>();
  private Map<String, HashSet<Integer>> modifiedFiles = new HashMap<>();
  private long lastChangeTimeMillis = 0;

  private List<CoverageMapping> coverageMappings = new ArrayList<>();

  public static synchronized DataStore getInstance() {
    return ourInstance;
  }

  private DataStore() {
  }

  public Project getActiveProject() {
    return activeProject;
  }

  public void setActiveProject(Project project) {
    this.activeProject = project;
  }

  public ChangedFile getLastChangedFile() {
    return lastChangedFile;
  }

  public void setLastChangedFile(ChangedFile lastChangedFile) {
    this.lastChangedFile = lastChangedFile;
  }

  public void initChangedFile() {
    this.lastChangedFile = new ChangedFile();
  }

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

  public Map<String, HashSet<Integer>> getModifiedFiles() {
    return modifiedFiles;
  }

  public Map<String, HashSet<Integer>> resetModifiedFiles() {
    return modifiedFiles =  new HashMap<>();
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

}
