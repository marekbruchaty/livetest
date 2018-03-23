package listeners;

import com.intellij.openapi.editor.event.DocumentEvent;
import com.intellij.openapi.editor.event.DocumentListener;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import resources.DataStore;

import java.util.logging.Logger;

public class LivetestDocumentListener implements DocumentListener {

    private static final Logger log = Logger.getLogger(LivetestDocumentListener.class.getName());

    @Override public void beforeDocumentChange(DocumentEvent event) {
//        log.info(String.format("File '%s' is going to be modified.",
//            FileDocumentManager.getInstance().getFile(event.getDocument()).getName()));
//        log.info(String.format("Document going to be changed: %s", event.getDocument().getText()));
        System.out.println("event.getNewLength(): " + event.getNewLength());
        System.out.println("event.getNewFragment(): " + event.getNewFragment());
        System.out.println("event.getOldLength(): " + event.getOldLength());
        System.out.println("event.getOldFragment(): " + event.getOldFragment());
        System.out.println("event.getOffset(): " + event.getOffset());
    }

    @Override
    public void documentChanged(DocumentEvent event) {
//        log.info(String.format("File '%s' has been modified.",
//            FileDocumentManager.getInstance().getFile(event.getDocument()).getName()));
//        log.info(String.format("Document changed: %s", event.getDocument().getText()));
        System.out.println("event.getNewLength(): " + event.getNewLength());
        System.out.println("event.getNewFragment(): " + event.getNewFragment());
        System.out.println("event.getOldLength(): " + event.getOldLength());
        System.out.println("event.getOldFragment(): " + event.getOldFragment());
        System.out.println("event.getOffset(): " + event.getOffset());
    }
}
