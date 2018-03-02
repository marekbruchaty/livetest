package resources;

import com.intellij.openapi.project.Project;
import model.ChangedFile;

public class DataStore {

  private static DataStore ourInstance = new DataStore();

  private Project activeProject;
  private ChangedFile lastChangedFile = new ChangedFile();

  public static DataStore getInstance() {
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

  public static DataStore getOurInstance() {
    return ourInstance;
  }

  public static void setOurInstance(DataStore ourInstance) {
    DataStore.ourInstance = ourInstance;
  }

  public ChangedFile getLastChangedFile() {
    return lastChangedFile;
  }

}
