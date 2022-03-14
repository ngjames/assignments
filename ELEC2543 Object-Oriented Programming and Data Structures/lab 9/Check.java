import java.util.zip.CheckedInputStream;

public class Check {
  private String Payee;
  private int Amount;
  private MyDate Date;
  private int CheckNumber;
  private static int counter = 1001;

  public Check(String name, int amt, MyDate date) {
    Payee = name;
    Amount = amt;
    Date = date;
    CheckNumber = counter;
    counter++;
  }

  public int getAmount() {
    return Amount;
  }

  public MyDate getDate() {
    return Date;
  }

  public int getCheckNumber() {
    return CheckNumber;
  }

  public String getPayee() {
    return Payee;
  }
}
