// YOU SHOULD NOT MODIFY THIS FILE
public class Lab7Main {

  public static void main(String[] args) {

    // Fraction
    Fraction fractions[] = new Fraction[5];
    fractions[0] = new Fraction(1, 2);
    fractions[1] = new Fraction(4, 5);
    fractions[2] = new Fraction(6, 11);
    fractions[3] = new Fraction(9, 4);
    fractions[4] = new Fraction(11, 8);
    System.out.println("The largest fraction is " + FindLargest.findLargest(fractions));

    System.out.println(fractions[0] + " + " + fractions[1] + " = " + fractions[0].add(fractions[1]));

    // MyDate
    MyDate dates[] = new MyDate[10];
    dates[0] = new MyDate(1997, 7, 1);
    dates[1] = new MyDate(1911, 10, 10);
    dates[2] = new MyDate(1945, 8, 15);
    dates[3] = new MyDate(1842, 8, 29);
    dates[4] = new MyDate(1898, 6, 9);
    dates[5] = new MyDate(1860, 10, 18);
    dates[6] = new MyDate(1962, 9, 1);
    dates[7] = new MyDate(2003, 4, 1);
    dates[8] = new MyDate(2011, 8, 18);
    dates[9] = new MyDate(1910, 3, 16);
    System.out.println("The latest date is " + FindLargest.findLargest(dates));

  }
}

