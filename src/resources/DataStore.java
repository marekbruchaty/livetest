package resources;

import com.intellij.openapi.project.Project;

public class DataStore {

  private static DataStore ourInstance = new DataStore();

  public static DataStore getInstance() {
    return ourInstance;
  }

  private Project activeProject;

  private DataStore() {
  }

  public Project getActiveProject() {
    return activeProject;
  }

  public void setActiveProject(Project project) {
    this.activeProject = project;
  }
}
