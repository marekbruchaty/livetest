package editor;

import com.intellij.openapi.editor.Document;
import com.intellij.openapi.editor.impl.DocumentMarkupModel;
import com.intellij.openapi.editor.markup.MarkupModel;
import com.intellij.openapi.editor.markup.RangeHighlighter;
import com.intellij.openapi.editor.markup.TextAttributes;
import com.intellij.openapi.fileEditor.FileEditor;
import com.intellij.openapi.fileEditor.FileEditorManager;
import com.intellij.openapi.fileEditor.TextEditor;
import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.ui.JBColor;
import com.intellij.util.DocumentUtil;
import org.bouncycastle.crypto.prng.RandomGenerator;
import resources.DataStore;

import java.awt.*;
import java.util.Arrays;
import java.util.Optional;
import java.util.stream.Stream;

/**
 * Utility class with static members used to interact with the editors highlighting features
 */
public class Highlighter {

    private static final Color highlightColor = Color.DARK_GRAY;

    private Highlighter() {
    }

    public static void highlightLine(VirtualFile virtualFile, Document document, int lineNumber) {
        MarkupModel markupModel = DocumentMarkupModel
            .forDocument(document, DataStore.getInstance().getActiveProject(), true);

        FileEditor[] editors =
            FileEditorManager.getInstance(DataStore.getInstance().getActiveProject())
                .getEditors(virtualFile);

        for (FileEditor editor : editors) {
            if (editor instanceof TextEditor) {
                TextAttributes textAttributes = new TextAttributes();
                textAttributes.setBackgroundColor(highlightColor);
                markupModel.addLineHighlighter(lineNumber, 0, textAttributes);
            }
        }
    }

    public static void removeLineHighlight(VirtualFile virtualFile, int lineNumber,
        MarkupModel markupModel) {
        //        FileEditor[] editors =
        //            FileEditorManager.getInstance(DataStore.getInstance().getActiveProject())
        //                .getEditors(virtualFile);

        Optional<RangeHighlighter> highlighters =
            Arrays.stream(markupModel.getAllHighlighters()).filter(x -> x.getLayer() == 0)
                .findAny();
        markupModel.removeHighlighter(highlighters.get());
        //        DocumentUtil.getLineTextRange();

        //        for (FileEditor editor : editors) {
        //            if (editor instanceof TextEditor) {
        //                TextAttributes textAttributes = new TextAttributes();
        //                textAttributes.setBackgroundColor(highlightColor);
        //                markupModel.addLineHighlighter(lineNumber, 0, textAttributes);
        //                markupModel.removeHighlighter();
        //
        //            }
        //        }
    }

}
