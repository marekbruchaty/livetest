package listeners;

import com.intellij.openapi.editor.Document;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.openapi.vfs.VirtualFileEvent;
import com.intellij.openapi.vfs.VirtualFileListener;
import model.FileLine;
import org.jetbrains.annotations.NotNull;
import resources.DataStore;

import java.util.ArrayList;
import java.util.logging.Logger;

public class LivetestFileListener implements VirtualFileListener {

    private final static Logger log = Logger.getLogger(LivetestFileListener.class.getName());

    public LivetestFileListener() {
        log.info("listeners.LivetestFileListener instantiated");
    }

    @Override public void beforeContentsChange(@NotNull VirtualFileEvent event) {
        if (isPythonFile(event.getFile())) {
            DataStore.getInstance().initChangedFile();
            DataStore.getInstance().getLastChangedFile().setOriginalContent(getTest(event));
        }
    }

    @Override public void contentsChanged(@NotNull VirtualFileEvent event) {
        if (isPythonFile(event.getFile())) {
            DataStore.getInstance().getLastChangedFile().setModifiedContent(getTest(event));

            ArrayList<FileLine> changes =
                DataStore.getInstance().getLastChangedFile().getChangedSequences();
        }
    }

    @Override public void beforeFileDeletion(@NotNull VirtualFileEvent event) {
        if (isPythonFile(event.getFile())) {
            getTest(event);
        }
    }

    @NotNull private VirtualFile getVirtualFile(@NotNull VirtualFileEvent event) {
        VirtualFile file = event.getFile();
        log.info(String.format("File '%s' has been modified.", file.getName()));
        return file;
    }

    private String getTest(VirtualFileEvent fileEvent) {
        Document document = FileDocumentManager.getInstance().getDocument(fileEvent.getFile());
        return document != null ? document.getText() : null;
    }

    private boolean isPythonFile(VirtualFile file) {
        return file.getExtension().equalsIgnoreCase("py");
    }
}
