package init;

import actions.HelloAction;
import com.intellij.openapi.components.ApplicationComponent;
import com.intellij.openapi.project.ProjectManager;
import com.intellij.openapi.vfs.VirtualFileManager;
import java.util.logging.Logger;
import listeners.LivetestFileListener;
import org.jetbrains.annotations.NotNull;

public class PluginInitialization implements ApplicationComponent {

  private static final Logger LOGGER = Logger.getLogger(HelloAction.class.getName());

  @Override
  public void initComponent() {
    LOGGER.info("Component initialization");

    VirtualFileManager.getInstance().addVirtualFileListener(new LivetestFileListener());

    ProjectManager.getInstance().getOpenProjects();

//    PsiManager.getInstance(ProjectManager.getInstance().getOpenProjects()[1]).addPsiTreeChangeListener();

  }

  @Override
  public void disposeComponent() {
    LOGGER.info("Component disposal");
  }

  @Override
  @NotNull
  public String getComponentName() {
    return "init.PluginInitialization";
  }
}
