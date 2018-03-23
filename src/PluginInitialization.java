import com.intellij.openapi.components.ApplicationComponent;
import com.intellij.openapi.editor.EditorFactory;
import com.intellij.openapi.editor.event.EditorEventMulticaster;
import com.intellij.openapi.editor.impl.event.EditorEventMulticasterImpl;
import com.intellij.openapi.project.ProjectManager;
import com.intellij.openapi.vfs.VirtualFileManager;
import listeners.LivetestDocumentListener;
import listeners.LivetestFileListener;
import listeners.LivetestProjectManagerListenerImpl;
import org.jetbrains.annotations.NotNull;

import java.util.logging.Logger;

public class PluginInitialization implements ApplicationComponent {

  private static final Logger log = Logger.getLogger(PluginInitialization.class.getName());

  @Override
  public void initComponent() {
    initListeners();
  }

  private void initListeners() {
//    ProjectManager.getInstance().addProjectManagerListener(new LivetestProjectManagerListenerImpl()); // Project info
//    VirtualFileManager.getInstance().addVirtualFileListener(new LivetestFileListener()); // File change info
    EditorFactory.getInstance().getEventMulticaster().addDocumentListener(new LivetestDocumentListener()); // File change info - only one working for difference
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
