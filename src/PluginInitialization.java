import com.intellij.openapi.components.ApplicationComponent;
import com.intellij.openapi.project.ProjectManager;
import com.intellij.openapi.vfs.VirtualFileManager;
import com.intellij.psi.PsiManager;
import listeners.LivetestFileListener;
import listeners.LivetestProjectManagerListenerImpl;
import org.jetbrains.annotations.NotNull;
import resources.DataStore;

import java.util.logging.Logger;

public class PluginInitialization implements ApplicationComponent {

  private static final Logger log = Logger.getLogger(PluginInitialization.class.getName());

  @Override
  public void initComponent() {
    initListeners();
//    PsiManager.getInstance(DataStore.getInstance().getActiveProject()).addPsiTreeChangeListener(null);
  }

  private void initListeners() {
    ProjectManager.getInstance().addProjectManagerListener(new LivetestProjectManagerListenerImpl()); // Project info
    VirtualFileManager.getInstance().addVirtualFileListener(new LivetestFileListener()); // File change info
  }

  @Override
  public void disposeComponent() {
    log.info("Component disposal");
  }

  @Override
  @NotNull
  public String getComponentName() {
    return "PluginInitialization";
  }
}
