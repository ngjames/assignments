public class Fraction implements Comparable, Addable {

  private int numerator, denominator;
 
  public Fraction(int num, int denom) {
    numerator = num;
    denominator = denom;
  }

  public double value() {
    return (double) numerator / denominator;
  }

  public String toString() {
    return Integer.toString(numerator) + "/" + Integer.toString(denominator);
  }

  public int compareTo(Object other) {
    Fraction fraction = (Fraction) other;
    if (this.value() > fraction.value()) {
      return 1;
    } else if (this.value() < fraction.value()) {
      return -1;
    } else {
      return 0;
    }
  }

  public Object add(Addable obj) {
    Fraction fraction = (Fraction) obj;
    Fraction temp = new Fraction(this.numerator*fraction.denominator+this.denominator*fraction.numerator, this.denominator * fraction.denominator);
    return temp;
  }
  
}
