import java.util.ArrayList; //add ArrayList as a datatype

public class CheckSummary {
  public static void printSummary(ArrayList<Check> checks) {

    int lastCheckNumber = 1000;
    int totalAmount = 0; //init variables

    for (Check check : checks) {
      System.out.println("Check No: " + check.getCheckNumber()+", Payee: " + check.getPayee() + ", Amount: " + check.getAmount() + ", Date: " + check.getDate());
      lastCheckNumber++;
      totalAmount += check.getAmount();
    }
    System.out.println("The next check number is " + (lastCheckNumber+1));
    System.out.println("");

    boolean firstCheck = true;
    int currentYear = 1;
    int currentMonth = 2;
    int currentMonthTotal = 3;
    int nextYear = 4;
    int nextMonth = 5;
    int nextMonthTotal = 0;
    // variables to support the next section

    for (Check check : checks) {
      if (firstCheck) {
        currentYear = check.getDate().getYear();
        currentMonth = check.getDate().getMonth();
        currentMonthTotal = check.getAmount();
        firstCheck = false;
      } else {
        nextYear = check.getDate().getYear();
        nextMonth = check.getDate().getMonth();
        nextMonthTotal = check.getAmount();

        if (currentYear == nextYear && currentMonth == nextMonth) {
          currentMonthTotal += nextMonthTotal;
        } else {
          System.out.println("The total amount of the checks issued in " + currentYear + '/' + currentMonth + " is " + currentMonthTotal);
          currentYear = nextYear;
          currentMonth = nextMonth;
          currentMonthTotal = nextMonthTotal;
        }
      }
    }
    //outside of for loop, requires 1 final run
    System.out.println("The total amount of the checks issued in " + currentYear + '/' + currentMonth + " is " + currentMonthTotal);
    System.out.println("The total amount is " + totalAmount);
  }

}
