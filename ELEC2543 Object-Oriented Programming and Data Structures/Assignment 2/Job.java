public class Job {

    private static int counter = 1;
    private int servedTimeNeeded;
    private int totalTimeServed = 0;
    private int id;


    public Job(int servedTimeNeeded) {
        this.servedTimeNeeded = servedTimeNeeded;
        this.id = counter;
        counter++;
    }

    public int served(int servedTime) {
        totalTimeServed += servedTime;
        return servedTimeNeeded - totalTimeServed;
    }

    public String toString() {
        String result = id + ":(" + servedTimeNeeded + "," + totalTimeServed + ")";
        return result;
    }

}