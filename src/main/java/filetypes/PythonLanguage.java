package filetypes;

import com.intellij.lang.Language;
import org.jetbrains.annotations.NotNull;

public class PythonLanguage extends Language {
  @NotNull
  public static final PythonLanguage INSTANCE = new PythonLanguage();

  private PythonLanguage() {
    super("PYTHON", "text/x-python-source", "text/python", "application/x-python", "text/x-python");
  }

  @NotNull
  @Override
  public String getDisplayName() {
    return "Python";
  }

  @Override
  public boolean isCaseSensitive() {
    return true;
  }
}
