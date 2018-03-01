package actions;

import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.project.Project;
import com.intellij.openapi.ui.Messages;
import utils.FileUtils;

import java.util.logging.Logger;

public class PluginStatus extends AnAction {

    private final static Logger LOGGER = Logger.getLogger(PluginStatus.class.getName());

    public PluginStatus() {
        super("Hello");
    }

    @Override
    public void actionPerformed(AnActionEvent e) {
        LOGGER.info("Hello action activated.");
        Project project = e.getProject();
        FileUtils.getAllProjectFiles(project);
//        Messages.showMessageDialog(project, "Hello world!", "Greeting", Messages.getInformationIcon());
    }
}
