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
import java.util.logging.Logger;

public class VirtualFileUtils {

    private VirtualFileUtils() {
    }

    private static final Logger log = Logger.getLogger(VirtualFileUtils.class.getName());

    public static void getAllProjectFiles(Project project) {
        log.info("Base directory: " + project.getBaseDir());

        VirtualFile[] children = project.getProjectFile().getChildren();
        log.info("Number of children: " + children.length);

        Collection<VirtualFile> files =
            FileTypeIndex.getFiles(PythonFileType.INSTANCE, GlobalSearchScope.allScope(project));

        log.info(() -> "Number of files in project: " + files.size());
        for (VirtualFile f : files) {
            log.info("file name: " + f.getName());
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
