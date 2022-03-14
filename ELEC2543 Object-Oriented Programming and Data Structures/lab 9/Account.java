import java.util.ArrayList;

public class Account {

  private int balance;

  public Account(int initialBalance) {
    balance = initialBalance;
  }

  public void processCheck(Check check) throws NotEnoughFundException {
    System.out.println("Processing Check No: " + check.getCheckNumber() + ", Payee: "+ check.getPayee() + ", Amount: "+ check.getAmount() + ", Date: "+ check.getDate());
     
    if (check.getAmount() > balance) {
      throw new NotEnoughFundException();
    } else {
      balance -= check.getAmount();
    }
  }

  public void processTransaction(ArrayList<Check> checks) {

    int i = 0;
    int j = checks.size();
    System.out.println("The current balance is " + balance);
    System.out.println("");
    while (i < j) {
      try {
        processCheck(checks.get(i));
        i++;
      } catch(NotEnoughFundException N) {
        System.out.println("check cannot be cleared due to not enough fund.");
        System.out.println("add 500 to the account...");
        balance += 500;
      } finally {
        System.out.println("The current balance is " + balance);
        System.out.println("");
      }
    }
  }
}
