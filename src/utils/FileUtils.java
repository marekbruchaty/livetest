package utils;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class FileUtils {

    public static List<String> readLines(String filePath) throws IOException {
        return FileUtils.readLines(new File(filePath));
    }

    public static List<String> readLines(File file) throws IOException {
        if (!file.exists()) {
            return new ArrayList<>();
        }

        List<String> results = new ArrayList<>();
        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(file));
            String line = reader.readLine();
            while (line != null) {
                results.add(line);
                line = reader.readLine();
            }
        } finally {
            if (reader != null) {
                reader.close();
            }
        }
        return results;
    }

}
