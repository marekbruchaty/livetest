package listeners;

import com.intellij.psi.PsiTreeChangeEvent;
import com.intellij.psi.PsiTreeChangeListener;
import org.jetbrains.annotations.NotNull;

import java.util.logging.Level;
import java.util.logging.Logger;

public class LivetestPsiTreeChangeListenerImpl implements PsiTreeChangeListener {

    private static final Logger log =
        Logger.getLogger(LivetestPsiTreeChangeListenerImpl.class.getName());

    public LivetestPsiTreeChangeListenerImpl() {
        super();
        log.setLevel(Level.OFF);
    }

    @Override public void beforeChildAddition(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.log(Level.FINE, String.format("beforeChildAddition | PsiTreeChangeEvent: %s", psiTreeChangeEvent));
//        Document document =
//            PsiDocumentManager.getInstance(DataStore.getInstance().getActiveProject())
//                .getDocument(psiTreeChangeEvent.getFile());
//        System.out.println("beforeChildAddition: " + document.getText());

    }

    @Override public void beforeChildRemoval(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(String.format("beforeChildRemoval | PsiTreeChangeEvent: %s", psiTreeChangeEvent));

    }

    @Override public void beforeChildReplacement(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(
            String.format("beforeChildReplacement | PsiTreeChangeEvent: %s", psiTreeChangeEvent));

    }

    @Override public void beforeChildMovement(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(String.format("beforeChildMovement | PsiTreeChangeEvent: %s", psiTreeChangeEvent));

    }

    @Override public void beforeChildrenChange(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(
            String.format("beforeChildrenChange | PsiTreeChangeEvent: %s", psiTreeChangeEvent));
//        Document document =
//            PsiDocumentManager.getInstance(DataStore.getInstance().getActiveProject())
//                .getDocument(psiTreeChangeEvent.getFile());
//        System.out.println("beforeChildrenChange: " + document.getText());

    }

    @Override public void beforePropertyChange(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(
            String.format("beforePropertyChange | PsiTreeChangeEvent: %s", psiTreeChangeEvent));

    }

    @Override public void childAdded(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(String.format("childAdded | PsiTreeChangeEvent: %s", psiTreeChangeEvent));
//        Document document =
//            PsiDocumentManager.getInstance(DataStore.getInstance().getActiveProject())
//                .getDocument(psiTreeChangeEvent.getFile());
//        System.out.println("childAdded: " + document.getText());

        
    }

    @Override public void childRemoved(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(String.format("childRemoved | PsiTreeChangeEvent: %s", psiTreeChangeEvent));

    }

    @Override public void childReplaced(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(String.format("childReplaced | PsiTreeChangeEvent: %s", psiTreeChangeEvent));

    }

    @Override public void childrenChanged(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(String.format("childrenChanged | PsiTreeChangeEvent: %s", psiTreeChangeEvent));

    }

    @Override public void childMoved(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(String.format("childMoved | PsiTreeChangeEvent: %s", psiTreeChangeEvent));

    }

    @Override public void propertyChanged(@NotNull PsiTreeChangeEvent psiTreeChangeEvent) {
        log.info(String.format("propertyChanged | PsiTreeChangeEvent: %s", psiTreeChangeEvent));
        //
    }
}
