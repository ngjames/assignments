// a class for representing dates
public class MyDate implements Comparable {
  private int year, month, day;

  // constructor
  public MyDate(int year, int month, int day) {
    this.year = year;
    this.month = month;
    this.day = day;
  }

  public int getYear() { return year; }

  public int getMonth() { return month; }

  public int getDay() { return day; }

  // print out date in the form of DD/MM/YYYY
  // no preceding zero for DD and MM
  public String toString() {
    return day + "/" + month + "/" + year;
  }

  public int compareTo(Object other) {
    MyDate otherDate = (MyDate) other;
    if (this.getYear() > otherDate.getYear()) {
      return 1;
    }
    if (this.getYear() < otherDate.getYear()) {
      return -1;
    } //same year
    if (this.getMonth() > otherDate.getMonth()) {
      return 1;
    }
    if (this.getMonth() < otherDate.getMonth()) {
      return -1;
    } //same month
    if (this.getDay() > otherDate.getDay()) {
      return 1;
    }
    if (this.getDay() < otherDate.getDay()) {
      return -1;
    }
    return 0; //same day

  }
}
