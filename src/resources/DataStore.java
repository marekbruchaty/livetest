package resources;

import com.intellij.openapi.project.Project;
import model.ChangedFile;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DataStore {

  private static DataStore ourInstance = new DataStore();

  private Project activeProject;
  private ChangedFile lastChangedFile = new ChangedFile();
  private Map<String, List<String>> unmodifiedFiles = new HashMap<>();
  private Map<String, List<Integer>> modifiedFiles = new HashMap<>();

  private DataStore() {
  }

  public Project getActiveProject() {
    return activeProject;
  }

  public void setActiveProject(Project project) {
    this.activeProject = project;
  }

  public static DataStore getInstance() {
    return ourInstance;
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

  public Map<String, List<Integer>> getModifiedFiles() {
    return modifiedFiles;
  }

  public void setModifiedFiles(Map<String, List<Integer>> modifiedFiles) {
    this.modifiedFiles = modifiedFiles;
  }
}
