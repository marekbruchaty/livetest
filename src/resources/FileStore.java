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

    public void addUnmodifiedFile(String path, List<String> lines) {
        this.unmodifiedFiles.put(path, lines);
    }

    public boolean existsUnmodifiedFile(String path) {
        return unmodifiedFiles.containsKey(path);
    }

    public String getUnmodifiedFile(String path, int lineIndex) {
        List<String> lines = unmodifiedFiles.get(path);
        if (lines == null)
            return null;
        return lines.get(lineIndex);
    }
}
