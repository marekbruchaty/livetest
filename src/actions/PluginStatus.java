package actions;

import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.project.Project;
import utils.VirtualFileUtils;

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
        VirtualFileUtils.getAllProjectFiles(project);
//        Messages.showMessageDialog(project, "Hello world!", "Greeting", Messages.getInformationIcon());
    }
}
