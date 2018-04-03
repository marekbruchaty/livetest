package listeners;

import com.intellij.openapi.project.Project;
import com.intellij.openapi.project.VetoableProjectManagerListener;
import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.psi.PsiManager;
import com.intellij.psi.search.FileTypeIndex;
import com.intellij.psi.search.GlobalSearchScope;
import com.intellij.util.indexing.FileBasedIndex;
import com.jetbrains.python.PythonFileType;
import org.jetbrains.annotations.NotNull;
import resources.DataStore;

import java.util.Collection;
import java.util.Objects;
import java.util.logging.Logger;

public class LivetestProjectManagerListenerImpl implements VetoableProjectManagerListener {

    private static final Logger log =
        Logger.getLogger(LivetestProjectManagerListenerImpl.class.getName());

    @Override public void projectOpened(Project project) {
        log.info(String.format("Active project name: %s, base path: %s", project.getName(),
            project.getBasePath()));

        DataStore.getInstance().setActiveProject(project);
        initListeners(project); // Init listeners dependent on current project

        log.info("Project base dir. canonical path: " + getProjectPath());
        log.info("Project base dir. name: " + getProjectName());

        logAllPyFiles();
    }

    @NotNull private String getProjectName() {
        return DataStore.getInstance().getActiveProject().getBaseDir().getName();
    }

    private void logAllPyFiles() {
        String fileLog = getAllProjectPyFiles().stream()
            .filter(x -> Objects.requireNonNull(x.getCanonicalPath()).startsWith(getProjectPath()))
            .map(x -> String.format("File name: %s,\tpath: %s\n", x.getName(), x.getCanonicalPath()))
            .reduce("", String::concat);

        log.info("All project files:\n" + fileLog);

    }

    private String getProjectPath() {
        return DataStore.getInstance().getActiveProject().getBaseDir().getCanonicalPath();
    }

    private Collection<VirtualFile> getAllProjectPyFiles() {
        return FileBasedIndex.getInstance()
            .getContainingFiles(FileTypeIndex.NAME, PythonFileType.INSTANCE,
                GlobalSearchScope.allScope(DataStore.getInstance().getActiveProject()));
    }

    private void initListeners(Project project) {
        PsiManager.getInstance(project)
            .addPsiTreeChangeListener(new LivetestPsiTreeChangeListenerImpl());
    }

    @Override public void projectClosing(Project project) {
        //TODO Plugin cleanup
    }

    @Override public boolean canClose(@NotNull Project project) {
        return false;
    }
}
