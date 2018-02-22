import com.intellij.openapi.actionSystem.*;
import com.intellij.openapi.project.Project;
import com.intellij.openapi.ui.Messages;
import java.util.logging.Logger;

public class HelloAction extends AnAction {

  private final static Logger LOGGER = Logger.getLogger(HelloAction.class.getName());

  public HelloAction() {
    super("Hello");
  }

  public void actionPerformed(AnActionEvent event) {
    Project project = event.getData(PlatformDataKeys.PROJECT);
    LOGGER.info("Hello action activated.");
    Messages.showMessageDialog(project, "Hello world!", "Greeting", Messages.getInformationIcon());
  }
}