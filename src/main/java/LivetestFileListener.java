import com.intellij.openapi.vfs.VirtualFileEvent;
import com.intellij.openapi.vfs.VirtualFileListener;
import java.util.logging.Logger;
import org.jetbrains.annotations.NotNull;

public class LivetestFileListener implements VirtualFileListener {

  private final static Logger LOGGER = Logger.getLogger(HelloAction.class.getName());

  public LivetestFileListener() {
    LOGGER.info("LivetestFileListener instantiated");
  }

  @Override
  public void contentsChanged(@NotNull VirtualFileEvent event) {
    LOGGER.info("File '" + event.getFileName() + "' has been modified.");
  }
}
