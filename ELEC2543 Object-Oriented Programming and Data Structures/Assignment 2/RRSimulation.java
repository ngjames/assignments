public class RRSimulation {
 
  // NO MORE INSTANCE VARIABLE CAN BE DEFINED
  private Ring jobs;

  // DO NOT MODIFY THE CONSTRUCTOR
  public RRSimulation() {
    jobs = GenJob.genInitJobList();
    System.out.println("The original job list is:");
    System.out.println(jobs);
  }

  public void run(int unit) {
    Job j;
    int hrs = 0;
    while (jobs.size() > 0) {
      Object jTemp = jobs.getCurrObj();
      j = (Job) jTemp;
      System.out.println("Job being served: " + j);
      int t = j.served(unit);
      hrs += unit;

      if (t <= 0) {
        System.out.println(j + " is done.");
        jobs.removeCurrObj();
      }
      System.out.println("The current job list is: "+ jobs);
      if (jobs.size() > 0) {
        jobs.advance();
      }
      
    }
    System.out.println("All jobs finished after " + hrs + " hours.");


  }

}
