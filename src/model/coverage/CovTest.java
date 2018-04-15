package model.coverage;

public class CovTest {
    private String name;
    private String filePath;
    private boolean passing;

    public CovTest(String name) {
        this.name = name;
        this.filePath = null;
        this.passing = false;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    public boolean isPassing() {
        return passing;
    }

    public void setPassing(boolean passing) {
        this.passing = passing;
    }
}
