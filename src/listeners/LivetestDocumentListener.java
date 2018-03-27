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

import java.util.Collections;
import java.util.logging.Level;
import java.util.logging.Logger;

public class LivetestDocumentListener implements DocumentListener {

    private static final Logger log = Logger.getLogger(LivetestDocumentListener.class.getName());

    @Override public void beforeDocumentChange(DocumentEvent event) {
        VirtualFile virtualFile = VirtualFileUtils.getVirtualFile(event.getDocument());
        if (!FileStore.getInstance().unmodifiedFileExists(virtualFile.getPath())) {
            FileStore.getInstance().addUnmodifiedFile(virtualFile.getPath(),
                Collections.singletonList(event.getDocument().getText()));
        }
    }

    @Override
    public void documentChanged(DocumentEvent event) {
        if (DataStore.getInstance().getActiveProject() == null) {
            log.log(Level.SEVERE, "No project found.");
            return;
        }

        String fileContent = event.getDocument().getText();
        int offset = event.getOffset();
        int lineNumber = StringUtils.countMatches(fileContent.substring(0, offset), "\n");

        VirtualFile virtualFile = VirtualFileUtils.getVirtualFile(event.getDocument());
        Highlighter.highlightLine(virtualFile, event.getDocument(), lineNumber);

        showInfoPopup(event, lineNumber);
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
