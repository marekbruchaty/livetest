package threads;

import resources.DataStore;

import java.util.Timer;
import java.util.TimerTask;
import java.util.logging.Level;
import java.util.logging.Logger;

public class TestCoverageThread extends Thread {

    private static final int PERIOD = 3000; // Wait 3 sec. between check
    private static final Logger LOGGER = Logger.getLogger(TestCoverageThread.class.getName());
    private DataStore ds = DataStore.getInstance();

    public TestCoverageThread() {
        super("threads.TestCoverageThread");
    }

    @Override public void run() {
        super.run();

        // Wait for project to load
        whileProjectNotReady();

        TimerTask timerTask = new TimerTask() {
            @Override public void run() {
                TestCoverageTask.getInstance().run();
            }
        };

        Timer timer = new Timer();
        timer.schedule(timerTask, 0, PERIOD);
    }

    private void whileProjectNotReady() {
        while (ds.getActiveProject() == null) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                new TestCoverageThread().start();
                LOGGER.log(Level.SEVERE, "Thread {0} interrupted forcefully. Thread restarted.",
                    Thread.currentThread().getName());
                Thread.currentThread().interrupt();
            }
        }
    }

    @Override public synchronized void start() {
        LOGGER.log(Level.INFO,
            "Thread " + getName() + " starting. Coverage run set to " + (PERIOD / 1000)
                + " second period", getName());
        super.start();
    }

}
