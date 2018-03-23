package resources;

import com.intellij.openapi.project.Project;
import listeners.LivetestProjectManagerListenerImpl;
import model.ChangedFile;

import java.util.logging.Logger;

public class DataStore {

  private static DataStore ourInstance = new DataStore();

  private Project activeProject;
  private ChangedFile lastChangedFile = new ChangedFile();

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
}
