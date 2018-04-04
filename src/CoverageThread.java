import resources.DataStore;

import java.util.Timer;
import java.util.TimerTask;

public class CoverageThread extends Thread {

    private static final int PERIOD = 3000; // 3 sec

    CoverageThread() {
        super("CoverageThread");
    }

    @Override public void run() {
        super.run();

        TimerTask timerTask = new TimerTask() {
            @Override public void run() {
                System.out.println("Timer task running on thread " + getName());
                if (DataStore.getInstance().getActiveProject() != null) {
                    System.out.println(getName() + " project from datastore " + DataStore.getInstance().getActiveProject().getName());
                }
            }
        };

        Timer timer = new Timer();
        timer.schedule(timerTask, 0, PERIOD);
    }

    @Override public synchronized void start() {
        super.start();
    }

}
