package editor;

import com.intellij.openapi.editor.Document;
import com.intellij.openapi.editor.impl.DocumentMarkupModel;
import com.intellij.openapi.editor.markup.GutterIconRenderer;
import com.intellij.openapi.editor.markup.MarkupModel;
import com.intellij.openapi.editor.markup.RangeHighlighter;
import com.intellij.openapi.editor.markup.TextAttributes;
import com.intellij.openapi.fileEditor.FileEditor;
import com.intellij.openapi.fileEditor.FileEditorManager;
import com.intellij.openapi.fileEditor.TextEditor;
import com.intellij.openapi.util.TextRange;
import com.intellij.util.DocumentUtil;
import icons.LivetestIcons;
import listeners.LivetestDocumentListener;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import resources.DataStore;
import utils.VirtualFileUtils;

import javax.swing.*;
import java.awt.*;
import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Utility class with static members used to interact with the editors highlighting features
 */
public class Highlighter {

    private static final Color highlightColor = Color.DARK_GRAY;
    private static final Logger log = Logger.getLogger(LivetestDocumentListener.class.getName());
    private static final int HIGHLIGHTER_LAYER = 66;

    private Highlighter() {
    }

    public static void addLineHighlight(Document document, int lineNumber) {
        if (highlightExists(document, lineNumber)) {
            log.log(Level.WARNING, "Highlighter for line {0} already exists!", lineNumber);
            return;
        }

        MarkupModel markupModel = getMarkupModel(document);

        FileEditor[] editors =
            FileEditorManager.getInstance(DataStore.getInstance().getActiveProject())
                .getEditors(VirtualFileUtils.getVirtualFile(document));

        for (FileEditor editor : editors) {
            if (editor instanceof TextEditor) {
                TextAttributes textAttributes = new TextAttributes();
                textAttributes.setBackgroundColor(highlightColor);
                textAttributes.setErrorStripeColor(highlightColor);
                RangeHighlighter highlighter =
                    markupModel.addLineHighlighter(lineNumber, HIGHLIGHTER_LAYER, textAttributes);

                addGutterIcon(highlighter, LivetestIcons.GutterIcons.Info);

            }
        }
    }

    private static void addGutterIcon(RangeHighlighter highlighter, Icon icon) {
        highlighter.setGutterIconRenderer(new GutterIconRenderer() {

            @Override public boolean equals(Object o) {
                return false;
            }

            @Override public int hashCode() {
                return 0;
            }

            @NotNull @Override public Icon getIcon() {
                return icon;
            }

            @Nullable @Override public String getTooltipText() {
                return "Cool, it works!";
            }
        });
    }

    public static void removeLineHighlight(Document document, int lineNumber) {
        MarkupModel markupModel = getMarkupModel(document);

        TextRange lineTextRange = DocumentUtil.getLineTextRange(document, lineNumber);

        for (RangeHighlighter highlighter : markupModel.getAllHighlighters()) {
            if (intersectsAndMatchLayer(highlighter, lineTextRange)) {
                markupModel.removeHighlighter(highlighter);
            }
        }
    }

    private static boolean intersectsAndMatchLayer(RangeHighlighter highlighter,
        TextRange lineTextRange) {
        return !(highlighter.getEndOffset() < lineTextRange.getStartOffset()
            || highlighter.getStartOffset() > lineTextRange.getEndOffset())
            && highlighter.getLayer() == HIGHLIGHTER_LAYER;
    }

    private static boolean highlightExists(Document document, int lineNumber) {
        return Arrays.stream(getMarkupModel(document).getAllHighlighters()).anyMatch(
            x -> intersectsAndMatchLayer(x, DocumentUtil.getLineTextRange(document, lineNumber)));
    }

    private static MarkupModel getMarkupModel(Document document) {
        return DocumentMarkupModel
            .forDocument(document, DataStore.getInstance().getActiveProject(), true);
    }

}
