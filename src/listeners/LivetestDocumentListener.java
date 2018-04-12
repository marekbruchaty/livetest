package listeners;

import com.intellij.openapi.editor.event.DocumentEvent;
import com.intellij.openapi.editor.event.DocumentListener;
import com.intellij.openapi.ui.MessageType;
import com.intellij.openapi.vfs.VirtualFile;
import editor.Highlighter;
import org.apache.commons.lang.StringUtils;
import resources.DataStore;
import resources.FileStore;
import utils.PopupUtils;
import utils.VirtualFileUtils;

import java.util.Arrays;
import java.util.Objects;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class LivetestDocumentListener implements DocumentListener {

    private static final Logger log = Logger.getLogger(LivetestDocumentListener.class.getName());

    @Override public void beforeDocumentChange(DocumentEvent event) {
        VirtualFile virtualFile = VirtualFileUtils.getVirtualFile(event.getDocument());
        if (!FileStore.getInstance().existsUnmodifiedFile(virtualFile.getPath())) {
            FileStore.getInstance().addUnmodifiedFile(virtualFile.getPath(),
                Arrays.stream(event.getDocument().getText().split("\n")).map(String::trim)
                    .collect(Collectors.toList()));
        }
    }

    @Override public void documentChanged(DocumentEvent event) {
        VirtualFile virtualFile = VirtualFileUtils.getVirtualFile(event.getDocument());

        if (!isPythonProjectFile(virtualFile)) {
            log.log(Level.INFO, String.format(
                "%s is and underscored file, not a python file or project file. Moving on...",
                virtualFile.getName()));
            return;
        }

        int lineNumber = getLineNumber(event.getDocument().getText(), event.getOffset());
        String newLine =
            Arrays.asList(event.getDocument().getText().split("\n")).get(lineNumber).trim();
        String oldLine =
            FileStore.getInstance().getUnmodifiedFile(virtualFile.getPath(), lineNumber);

        if (oldLine.equalsIgnoreCase(newLine)) {
            DataStore.getInstance().removeChangedLine(virtualFile.getPath(), lineNumber);
            Highlighter.removeLineHighlight(event.getDocument(), lineNumber);
        } else {
            DataStore.getInstance().addChangedLine(virtualFile.getPath(), lineNumber);
            DataStore.getInstance().resetLastChangeTimeMillis();
            Highlighter
                .addLineHighlight(event.getDocument(), lineNumber, Highlighter.HighlightType.EDIT,
                    "This is a modified line.");
        }

        //        showInfoPopup(event, lineNumber);
    }

    private boolean isPythonProjectFile(VirtualFile virtualFile) {
        System.out.println(virtualFile.getPath());
        System.out.println(virtualFile.getName());
        return virtualFile.getPath().startsWith(
            Objects.requireNonNull(DataStore.getInstance().getActiveProject().getBasePath()))
            && virtualFile.getName().toLowerCase().endsWith(".py") && !virtualFile.getName()
            .startsWith("__");
    }

    private int getLineNumber(String fileContent, int offset) {
        return StringUtils.countMatches(fileContent.substring(0, offset), "\n");
    }

    private void showInfoPopup(DocumentEvent event, int lineNumber) {
        String eventDetailInfo = getEventDetailInfo(event);
        eventDetailInfo += String.format("%nLine n.%d changed", lineNumber + 1);
        PopupUtils.createPopup(eventDetailInfo, MessageType.INFO);
    }

    private String getEventDetailInfo(DocumentEvent event) {
        return "\nevent.getNewLength(): " + event.getNewLength() + "\nevent.getNewFragment(): "
            + event.getNewFragment() + "\nevent.getOldLength(): " + event.getOldLength()
            + "\nevent.getOldFragment(): " + event.getOldFragment() + "\nevent.getOffset(): "
            + event.getOffset();
    }
}
