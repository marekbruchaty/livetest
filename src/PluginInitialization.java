import com.intellij.openapi.components.ApplicationComponent;
import com.intellij.openapi.editor.EditorFactory;
import com.intellij.openapi.project.ProjectManager;
import listeners.LivetestDocumentListener;
import listeners.LivetestProjectManagerListenerImpl;
import org.jetbrains.annotations.NotNull;
import threads.TestCoverageThread;

import java.util.logging.Logger;

public class PluginInitialization implements ApplicationComponent {

    private static final Logger log = Logger.getLogger(PluginInitialization.class.getName());

    @Override public void initComponent() {
        initListeners();
        initCoverageThread();
    }

    private void initCoverageThread() {
        new TestCoverageThread().start();
    }

    private void initListeners() {
        initProjectManagerListeners(); // Project info
        initDocumentListeners(); // File change info - can detect every file change
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
