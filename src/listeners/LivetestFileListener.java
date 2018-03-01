package listeners;

import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.openapi.vfs.VirtualFileEvent;
import com.intellij.openapi.vfs.VirtualFileListener;
import java.util.logging.Logger;

import org.jetbrains.annotations.NotNull;

public class LivetestFileListener implements VirtualFileListener {

  private final static Logger LOGGER = Logger.getLogger(LivetestFileListener.class.getName());

  public LivetestFileListener() {
    LOGGER.info("listeners.LivetestFileListener instantiated");
  }

  @Override
  public void beforeContentsChange(@NotNull VirtualFileEvent event) {
    VirtualFile file = event.getFile();
    LOGGER.info("File '" + file.getName() + "' has been modified.");
  }

  @Override
  public void contentsChanged(@NotNull VirtualFileEvent event) {
    VirtualFile file = event.getFile();
    LOGGER.info("File '" + file.getName() + "' has been modified.");
  }

  @Override
  public void beforeFileDeletion(@NotNull VirtualFileEvent event) {
    VirtualFile file = event.getFile();
    LOGGER.info("File '" + file.getName() + "' has been modified.");
  }
}
