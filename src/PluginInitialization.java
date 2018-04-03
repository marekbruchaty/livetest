import com.intellij.openapi.components.ApplicationComponent;
import com.intellij.openapi.editor.EditorFactory;
import com.intellij.openapi.project.ProjectManager;
import com.intellij.openapi.vfs.VirtualFileManager;
import listeners.LivetestDocumentListener;
import listeners.LivetestFileListener;
import listeners.LivetestProjectManagerListenerImpl;
import org.jetbrains.annotations.NotNull;

import java.util.Timer;
import java.util.TimerTask;
import java.util.logging.Logger;

public class PluginInitialization implements ApplicationComponent {

    private static final Logger log = Logger.getLogger(PluginInitialization.class.getName());

    @Override public void initComponent() {
        initListeners();
    }

    private void initListeners() {
        initProjectManagerListeners(); // Project info
        initDocumentListeners(); // File change info - can detect every file change
        initVirtualFileListeners(); // File change info
    }

    private void initVirtualFileListeners() {
//        VirtualFileManager.getInstance().addVirtualFileListener(new LivetestFileListener());
    }

    private void initDocumentListeners() {
        EditorFactory.getInstance().getEventMulticaster().addDocumentListener(
            new LivetestDocumentListener());
    }

    private void initProjectManagerListeners() {
        ProjectManager.getInstance()
            .addProjectManagerListener(new LivetestProjectManagerListenerImpl());
    }

    @Override public void disposeComponent() {
        log.info("Component disposal");
    }

    @Override @NotNull public String getComponentName() {
        return "PluginInitialization";
    }
}
