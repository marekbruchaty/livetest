package editor;

import colors.LivetestColors;
import com.intellij.openapi.editor.Document;
import com.intellij.openapi.editor.impl.DocumentMarkupModel;
import com.intellij.openapi.editor.markup.GutterIconRenderer;
import com.intellij.openapi.editor.markup.MarkupModel;
import com.intellij.openapi.editor.markup.RangeHighlighter;
import com.intellij.openapi.editor.markup.TextAttributes;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import com.intellij.openapi.fileEditor.FileEditor;
import com.intellij.openapi.fileEditor.FileEditorManager;
import com.intellij.openapi.fileEditor.TextEditor;
import com.intellij.openapi.util.TextRange;
import com.intellij.openapi.vfs.LocalFileSystem;
import com.intellij.openapi.vfs.VirtualFile;
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
import java.util.Optional;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Utility class with static members used to interact with the editors highlighting features
 */
public class Highlighter {

    private static final Logger LOGGER = Logger.getLogger(LivetestDocumentListener.class.getName());
    private static final int HIGHLIGHTER_LAYER = 66;

    private Highlighter() {
    }

    private static Color highlightColor = null;
    private static Icon highlightIcon = null;


    public enum HighlightType {
        INFO, EDIT, PASS, FAIL
    }


    public static void addLineHighlight(String filePath, Integer lineNumber, HighlightType type, boolean isModifiedLine,
        String tooltipText) {
        VirtualFile virtualFile = LocalFileSystem.getInstance().findFileByPath(filePath);
        if (virtualFile != null) {
            LOGGER.log(Level.INFO, "Adding highlighter for line number " + lineNumber + ", file " + filePath);
            addLineHighlight(FileDocumentManager.getInstance().getDocument(virtualFile), lineNumber - 1, type,
                isModifiedLine, tooltipText);
        } else {
            LOGGER.log(Level.SEVERE, "Cannot find VirtualFile while creating highlighter!");
        }
    }

    public static void addLineHighlight(Document document, int lineNumber, HighlightType type, boolean isModifiedLine,
        String tooltipText) {

        setupLineStyle(type);

        for (FileEditor editor : FileEditorManager.getInstance(DataStore.getInstance().getActiveProject())
            .getEditors(VirtualFileUtils.getVirtualFile(document))) {
            if (editor instanceof TextEditor && highlightIcon != null) {
                addGutterIcon(getRangeHighlighter(document, lineNumber, type, isModifiedLine), highlightIcon, tooltipText);
            }
        }
    }

    @NotNull private static RangeHighlighter getRangeHighlighter(Document document, int lineNumber, HighlightType type,
        boolean isModifiedLine) {
        MarkupModel markupModel = getMarkupModel(document);
        TextAttributes textAttributes = getTextAttributes();

        RangeHighlighter highlighter;
        Optional<RangeHighlighter> existingHighlight = getExistingHighlighter(document, lineNumber);
        if (existingHighlight.isPresent()) {
            highlighter = existingHighlight.get();

            if (isModifiedLine && type == HighlightType.FAIL) {
                markupModel.removeHighlighter(highlighter);
                highlighter = markupModel.addLineHighlighter(lineNumber, HIGHLIGHTER_LAYER, textAttributes);
            } else if (highlighter.getTextAttributes() != null) {
                markupModel.removeHighlighter(highlighter);
                highlighter = markupModel.addLineHighlighter(lineNumber, HIGHLIGHTER_LAYER, null);
            }

        } else {
            highlighter = markupModel.addLineHighlighter(lineNumber, HIGHLIGHTER_LAYER, textAttributes);
        }

        return highlighter;
    }

    @Nullable private static TextAttributes getTextAttributes() {
        TextAttributes textAttributes = null;
        if (highlightColor != null) {
            textAttributes = new TextAttributes();
            textAttributes.setBackgroundColor(highlightColor);
            textAttributes.setErrorStripeColor(highlightColor);
        }
        return textAttributes;
    }

    private static void setupLineStyle(HighlightType type) {
        if (type == HighlightType.INFO) {
            highlightIcon = LivetestIcons.GutterIcons.INFO;
            highlightColor = null;
        } else if (type == HighlightType.EDIT) {
            highlightIcon = LivetestIcons.GutterIcons.EDIT;
            highlightColor = null;
        } else if (type == HighlightType.PASS) {
            highlightIcon = LivetestIcons.GutterIcons.PASS;
            highlightColor = null;
        } else if (type == HighlightType.FAIL) {
            highlightIcon = LivetestIcons.GutterIcons.FAIL;
            highlightColor = LivetestColors.HighlightColors.FAIL;
        }
    }

    private static void addGutterIcon(RangeHighlighter highlighter, Icon icon, String tooltipText) {
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
                return tooltipText;
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

    private static boolean intersectsAndMatchLayer(RangeHighlighter highlighter, TextRange lineTextRange) {
        return !(highlighter.getEndOffset() < lineTextRange.getStartOffset()
            || highlighter.getStartOffset() > lineTextRange.getEndOffset())
            && highlighter.getLayer() == HIGHLIGHTER_LAYER;
    }

    private static Optional<RangeHighlighter> getExistingHighlighter(Document document, int lineNumber) {
        return Arrays.stream(getMarkupModel(document).getAllHighlighters())
            .filter(x -> intersectsAndMatchLayer(x, DocumentUtil.getLineTextRange(document, lineNumber))).findFirst();
    }

    private static MarkupModel getMarkupModel(Document document) {
        return DocumentMarkupModel.forDocument(document, DataStore.getInstance().getActiveProject(), true);
    }

}
