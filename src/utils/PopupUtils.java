package utils;

import com.intellij.openapi.ui.MessageType;
import com.intellij.openapi.ui.popup.Balloon;
import com.intellij.openapi.ui.popup.JBPopupFactory;
import com.intellij.openapi.wm.StatusBar;
import com.intellij.openapi.wm.WindowManager;
import com.intellij.ui.awt.RelativePoint;
import resources.DataStore;

public class PopupUtils {

    private PopupUtils() {
    }

    public static void createPopup(String text, MessageType messageType) {
        StatusBar statusBar =
            WindowManager.getInstance().getStatusBar(DataStore.getInstance().getActiveProject());

        JBPopupFactory.getInstance().createHtmlTextBalloonBuilder(text, messageType, null)
            .setFadeoutTime(2500).createBalloon()
            .show(RelativePoint.getSouthEastOf(statusBar.getComponent()), Balloon.Position.atLeft);
    }
}
