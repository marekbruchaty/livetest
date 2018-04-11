package icons;

import com.intellij.openapi.util.IconLoader;

import javax.swing.*;

public class LivetestIcons {

    public LivetestIcons() {
    }

    public static class GutterIcons {
        public static final Icon INFO = IconLoader.getIcon("/icons/gutter/livetestInfo.png");
        public static final Icon PASS = IconLoader.getIcon("/icons/gutter/livetestPass.png");
        public static final Icon FAIL = IconLoader.getIcon("/icons/gutter/livetestFail.png");

        public GutterIcons() {
        }
    }
}
