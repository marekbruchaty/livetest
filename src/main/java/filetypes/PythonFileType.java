package filetypes;

import com.intellij.openapi.fileTypes.LanguageFileType;
import javax.swing.Icon;
import org.jetbrains.annotations.NonNls;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public class PythonFileType extends LanguageFileType {
  @NonNls
  public static final String DEFAULT_EXTENSION = "py";
  @NonNls public static final String DOT_DEFAULT_EXTENSION = ".py";
  public static final PythonFileType INSTANCE = new PythonFileType();


  private PythonFileType() {
    super(PythonLanguage.INSTANCE);
  }

  @NotNull
  @Override
  public String getName() {
    return "PYTHON";
  }

  @NotNull
  @Override
  public String getDescription() {
    return "Python file type";
  }

  @NotNull
  @Override
  public String getDefaultExtension() {
    return DEFAULT_EXTENSION;
  }

  @Nullable
  @Override
  public Icon getIcon() {
    return null;
  }
}
