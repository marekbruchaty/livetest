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
import java.util.logging.Level;
import java.util.logging.Logger;

public class LivetestProjectManagerListenerImpl implements VetoableProjectManagerListener {

    private static final Logger log =
        Logger.getLogger(LivetestProjectManagerListenerImpl.class.getName());

    @Override public void projectOpened(Project project) {
//        log.setLevel(Level.INFO);
        log.info(String.format("Active project name: %s, base path: %s", project.getName(),
            project.getBasePath()));
        DataStore.getInstance().setActiveProject(project);

        initListeners(project); // Init listeners dependent on current project

        Collection<VirtualFile> allProjectFiles = FileBasedIndex.getInstance()
            .getContainingFiles(FileTypeIndex.NAME, PythonFileType.INSTANCE,
                GlobalSearchScope.allScope(DataStore.getInstance().getActiveProject()));

        VirtualFile baseDir = DataStore.getInstance().getActiveProject().getBaseDir();
        log.info(String.format("Project base dir: %s", baseDir.getCanonicalPath()));
        log.info(String.format("Project base dir: %s", baseDir.getName()));

        for (VirtualFile file : baseDir.getChildren()) {
            log.info(String.format("File base dir: %s\nFile base dir: %s", file.getCanonicalPath(),
                file.getName()));
        }

        log.info("All project files:");
        for (VirtualFile file : allProjectFiles) {
            if (file.getCanonicalPath().startsWith(baseDir.getCanonicalPath()) && file.getName()
                .toLowerCase().startsWith("test")) {
                log.info(
                    String.format("name: %s, path: %s", file.getName(), file.getCanonicalPath()));
            }
        }
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
