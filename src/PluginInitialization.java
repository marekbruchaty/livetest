import com.intellij.openapi.components.ApplicationComponent;
import com.intellij.openapi.project.ProjectManager;
import com.intellij.openapi.vfs.VirtualFileManager;
import listeners.LivetestFileListener;
import org.jetbrains.annotations.NotNull;

import java.util.logging.Logger;

public class PluginInitialization implements ApplicationComponent {

  private static final Logger LOGGER = Logger.getLogger(PluginInitialization.class.getName());

  @Override
  public void initComponent() {
    LOGGER.info("Component initialization");

    VirtualFileManager.getInstance().addVirtualFileListener(new LivetestFileListener());
//    ProjectManager.getInstance().getOpenProjects();

//    PsiManager.getInstance(ProjectManager.getInstance().getOpenProjects()[1]).addPsiTreeChangeListener();

  }

  @Override
  public void disposeComponent() {
    LOGGER.info("Component disposal");
  }

  @Override
  @NotNull
  public String getComponentName() {
    return "PluginInitialization";
  }
}
