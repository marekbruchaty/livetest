package listeners;

import com.intellij.openapi.editor.Document;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.openapi.vfs.VirtualFileEvent;
import com.intellij.openapi.vfs.VirtualFileListener;

import java.util.logging.Logger;

import org.jetbrains.annotations.NotNull;
import resources.DataStore;

public class LivetestFileListener implements VirtualFileListener {

    private final static Logger log = Logger.getLogger(LivetestFileListener.class.getName());

    public LivetestFileListener() {
        log.info("listeners.LivetestFileListener instantiated");
    }

    @Override
    public void beforeContentsChange(@NotNull VirtualFileEvent event) {
        if (isPythonFile(event.getFile())) {
            VirtualFile file = getVirtualFile(event);
            DataStore.getInstance().getLastChangedFile().setOriginalCharSequence(getFileCharSequence(file));
        }
    }

    @Override
    public void contentsChanged(@NotNull VirtualFileEvent event) {
        if (isPythonFile(event.getFile())) {
            VirtualFile file = getVirtualFile(event);
            DataStore.getInstance().getLastChangedFile().setModifiedCharSequence(getFileCharSequence(file));

            DataStore.getInstance().getLastChangedFile().getChangedSequences();
//            DataStore.getInstance().getLastChangedFile().printOrigFile();
//            DataStore.getInstance().getLastChangedFile().printModFile();
        }
    }

    @Override
    public void beforeFileDeletion(@NotNull VirtualFileEvent event) {
        if (isPythonFile(event.getFile())) {
            VirtualFile file = getVirtualFile(event);
            getFileCharSequence(file);
        }
    }

    @NotNull
    private VirtualFile getVirtualFile(@NotNull VirtualFileEvent event) {
        VirtualFile file = event.getFile();
        log.info(String.format("File '%s' has been modified.", file.getName()));
        return file;
    }

    private String
    getFileCharSequence(VirtualFile file) {
        Document document = FileDocumentManager.getInstance().getDocument(file);
        System.out.println("getImmutableCharSequence: " + document.getImmutableCharSequence());
        return document != null ? document.getImmutableCharSequence().toString() : null;
    }

    private boolean isPythonFile(VirtualFile file) {
        return file.getExtension().equalsIgnoreCase("py");
    }
}
