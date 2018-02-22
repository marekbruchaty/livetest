import com.intellij.openapi.components.ApplicationComponent;
import com.intellij.openapi.vfs.VirtualFileManager;
import java.util.logging.Logger;
import org.jetbrains.annotations.NotNull;

public class PluginInitialization implements ApplicationComponent {

  private final static Logger LOGGER = Logger.getLogger(HelloAction.class.getName());

  public PluginInitialization() {
  }

  @Override
  public void initComponent() {
    LOGGER.info("Component initialization");

    VirtualFileManager.getInstance().addVirtualFileListener(new LivetestFileListener());
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
