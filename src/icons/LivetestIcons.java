package icons;

import com.intellij.openapi.util.IconLoader;

import javax.swing.*;

public class LivetestIcons {

    public LivetestIcons() {
    }

    public static class GutterIcons {
        public static final Icon Info = IconLoader.getIcon("/icons/gutter/livetestInfo.png");
        public static final Icon Pass = IconLoader.getIcon("/icons/gutter/livetestPass.png");
        public static final Icon Fail = IconLoader.getIcon("/icons/gutter/livetestFail.png");

        public GutterIcons() {
        }
    }
}
