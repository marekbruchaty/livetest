package exceptions;

import enums.LivetestErrorCode;

public class LivetestException extends RuntimeException {
    public LivetestException(LivetestErrorCode errorCode) {
        super(errorCode.getMessage());
    }
}
