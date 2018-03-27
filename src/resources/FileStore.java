package resources;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FileStore {

  private static FileStore ourInstance = new FileStore();

  private Map<String, List<String>> unmodifiedFiles = new HashMap<>();

  private FileStore() {
  }

  public static FileStore getInstance() {
    return ourInstance;
  }

  public Map<String, List<String>> getUnmodifiedFiles() {
    return unmodifiedFiles;
  }

  public List<String> getUnmodifiedFileText(String key) {
    return unmodifiedFiles.get(key);
  }

  public void initUnmodifiedFiles() {
    this.unmodifiedFiles = new HashMap<>();
  }

  public boolean unmodifiedFileExists(String path) {
    return this.unmodifiedFiles.containsKey(path);
  }

  public void addUnmodifiedFile(String path, List<String> text) {
    this.unmodifiedFiles.put(path, text);
  }

}
