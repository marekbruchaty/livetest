package utils;

import com.intellij.openapi.project.Project;
import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.psi.search.FileTypeIndex;
import com.intellij.psi.search.GlobalSearchScope;
import filetypes.PythonFileType;
import java.util.Collection;
import java.util.logging.Logger;

public class FileUtils {

  private FileUtils() {
  }

  private static final Logger LOGGER = Logger.getLogger(FileUtils.class.getName());

  public static void getAllProjectFiles(Project project) {
    LOGGER.info("Base directory: " + project.getBaseDir());

    VirtualFile[] children = project.getProjectFile().getChildren();
    LOGGER.info("Number of children: " + children.length);

    Collection<VirtualFile> files = FileTypeIndex
        .getFiles(PythonFileType.INSTANCE, GlobalSearchScope.allScope(project));

    LOGGER.info(() -> "Number of files in project: " + files.size());
    for (VirtualFile f : files) {
      LOGGER.info("file name: " + f.getName());
    }
  }

}
