import java.text.spi.NumberFormatProvider;

public class Fraction {

  private int numerator, denominator;

  // method for finding the greatest common divisor of the parameters
  // e.g. gcd(15, 10) returns 5
  // You are recommended to pass positive parameters to this method
  // we will explain what "private" and "static" mean in later classes
  // you do not have to use this method if you do not want to
  Fraction(int Numerator, int Denominator) {
    this.numerator = Numerator;
    this.denominator = Denominator;
    if (denominator < 0) {
      denominator = -1*denominator;
      numerator = -1*numerator;
    }
    if (Numerator < 0) {
      if (Denominator < 0) {
        this.numerator = this.numerator / (gcd((-1)*Numerator, (-1)*Denominator));
        this.denominator = this.denominator / (gcd((-1)*Numerator, (-1)*Denominator)); 
      } else if (Denominator > 0 ) {
        this.numerator = this.numerator / (gcd((-1)*Numerator, Denominator));
        this.denominator = this.denominator / (gcd((-1)*Numerator, Denominator)); 
      }
    } else {
      if (Denominator > 0) {
        this.numerator = this.numerator / (gcd(Numerator, Denominator));
        this.denominator = this.denominator / (gcd(Numerator, Denominator)); 
      } else if (Denominator < 0) {
        this.numerator = this.numerator / (gcd(Numerator, (-1)*Denominator));
        this.denominator = this.denominator / (gcd(Numerator, (-1)*Denominator)); 
      }
    }



    if (numerator == 0) {
      denominator = 1;
    }
    if (denominator == 0) {
      if (!(numerator == 0)) {
        numerator = 1;
        denominator = 2;
      }
    }
  }

    

  private static int gcd(int a, int b) {

    if(a == 0 || b == 0) return a+b; // base case

    return gcd(b,a%b);
  }
  
  public double value() {
  return (double)numerator/(double)denominator;
  }

  public String toString() {
    return numerator + "/" + denominator;
  }
  

}
