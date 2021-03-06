package enums;

public enum LivetestErrorCode {
    NO_VIRTUAL_FILE_FOR_DOCUMENT("No virtual file found for document."),
    NO_ACTIVE_PROJECT_FOUND("No active project found."),
    NO_COVERAGE_FILE_AVAILABLE("No coverage file found on disk."),
    ERROR_OCCURRED_WHILE_SUBPROCESS_EXECUTION("Error occurred while executing subprocess.");

    private final String message;

    LivetestErrorCode(String message) {
        this.message = message;
    }

    public String getMessage() {
        return message;
    }

    public static boolean contains(String id) {
        for (LivetestErrorCode cdt : values()) {
            if(cdt.message.equals(id)) {
                return true;
            }
        }
        return false;
    }

}
