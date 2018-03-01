package listeners;

import actions.HelloAction;
import com.intellij.openapi.editor.event.DocumentEvent;
import com.intellij.openapi.editor.event.DocumentListener;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import java.util.logging.Logger;

public class LivetestDocumentListener implements DocumentListener {

  private static final Logger LOGGER = Logger.getLogger(HelloAction.class.getName());

  @Override
  public void documentChanged(DocumentEvent event) {
    LOGGER.info("File '" + FileDocumentManager.getInstance().getFile(event.getDocument()).getName()
        + "' has been modified.");
  }
}
