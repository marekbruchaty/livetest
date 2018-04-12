package utils;

import com.intellij.openapi.editor.Document;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import com.intellij.openapi.project.Project;
import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.psi.search.FileTypeIndex;
import com.intellij.psi.search.GlobalSearchScope;
import com.jetbrains.python.PythonFileType;
import enums.LivetestErrorCode;
import exceptions.LivetestException;

import java.util.Collection;
import java.util.logging.Level;
import java.util.logging.Logger;

public class VirtualFileUtils {

    private VirtualFileUtils() {
    }

    private static final Logger logger = Logger.getLogger(VirtualFileUtils.class.getName());

    public static void getAllProjectFiles(Project project) {
        logger.log(Level.INFO,"Base directory: {0}", project.getBaseDir());

        VirtualFile[] children = project.getProjectFile().getChildren();
        logger.log(Level.INFO, "Number of children: {0}", children.length);

        Collection<VirtualFile> files =
            FileTypeIndex.getFiles(PythonFileType.INSTANCE, GlobalSearchScope.allScope(project));

        logger.log(Level.INFO, "Number of files in project: {0}", files.size());
        for (VirtualFile f : files) {
            logger.log(Level.INFO,"file name: {0}", f.getName());
        }
    }

    public static VirtualFile getVirtualFile(Document document) {
        VirtualFile virtualFile = FileDocumentManager.getInstance().getFile(document);
        if (virtualFile == null) {
            throw new LivetestException(LivetestErrorCode.NO_VIRTUAL_FILE_FOR_DOCUMENT);
        }
        return virtualFile;
    }

}
