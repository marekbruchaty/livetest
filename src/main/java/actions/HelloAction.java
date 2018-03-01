package actions;

import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.actionSystem.PlatformDataKeys;
import com.intellij.openapi.project.Project;
import com.intellij.openapi.ui.Messages;
import java.io.File;
import java.util.logging.Logger;
import utils.FileUtils;

public class HelloAction extends AnAction {

  private final static Logger LOGGER = Logger.getLogger(HelloAction.class.getName());

  public HelloAction() {
    super("Hello");
  }

  public void actionPerformed(AnActionEvent event) {
    Project project = event.getProject();
    LOGGER.info("Hello action activated.");
    Messages.showMessageDialog(project, "Hello world!", "Greeting", Messages.getInformationIcon());
    FileUtils.getAllProjectFiles(project);
  }
}