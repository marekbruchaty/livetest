package listeners;

import com.intellij.openapi.project.Project;
import com.intellij.openapi.project.VetoableProjectManagerListener;
import org.jetbrains.annotations.NotNull;
import resources.DataStore;

import java.util.logging.Logger;

public class LivetestProjectManagerListenerImpl implements VetoableProjectManagerListener {

    private static final Logger log = Logger.getLogger(LivetestProjectManagerListenerImpl.class.getName());

    @Override
    public void projectOpened(Project project) {
        log.info(String.format("Active project name: %s, base path: %s", project.getName(), project.getBasePath()));
        DataStore.getInstance().setActiveProject(project);
    }

    @Override
    public void projectClosing(Project project) {
        //TODO Plugin cleanup
    }

    @Override
    public boolean canClose(@NotNull Project project) {
        return false;
    }
}
