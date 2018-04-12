package model.coverage;

public class CovTest {
    private String name;
    private String url;
    private boolean passing;

    public CovTest(String name, boolean passing) {
        this.name = name;
        this.url = null;
        this.passing = false;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public boolean passing() {
        return passing;
    }

    public void setPassing(boolean passing) {
        this.passing = passing;
    }
}
