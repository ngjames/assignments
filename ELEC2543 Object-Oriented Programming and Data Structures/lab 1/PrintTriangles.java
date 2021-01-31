import java.util.Scanner; // import Scanner class to read inputs

// "public" is a visibility modifier 
// we will study more about visibility modifiers later
public class PrintTriangles {

  // "private" is a visibility modifier
  // we will study more about visibility modifiers later
  // this method is "static" means this method belong to the class instead of an
  // individual object
  // we will study the meaning of "static" in details later
  // This method prints out the menu to ask for user input
  private static void printMenu() {
    System.out.println("This program prints a shape with a certain size of your choice.");
    System.out.println("You have to select the shape from one of the following:");
    System.out.println("0 -- right-angled triangle with the right angle in the lower left");
    System.out.println("1 -- right-angled triangle with the right angle in the upper left");
    System.out.println("2 -- right-angled triangle with the right angle in the lower right");
    System.out.println("3 -- a diamond");

    System.out.println(
        "After selecting the shape, you will be asked to input the size of the shape. For triangles, the size is the width and height of the triangle. This size must not be larger than 15. For diamonds, the size tells the number of * on the longest row. The size must be an odd number not larger than 15.\n");
  }

  // This method prints out the right-angled triangle
  // with the right angle in the lower left
  private static void printLLT(int size) {
    for (int i = 0; i < size; i++) {
      for (int j = 0; j <= i; j++)
        System.out.print("*");
      System.out.println();
    }
  }

  // This method prints out the right-angled triangle
  // with the right angle in the upper left
  private static void printULT(int size) {
    for (int i = size; i > 0; i--) {
      for (int j = i; j > 0; j--)
        System.out.print("*");
      System.out.println();
    }
  }

  // This method prints out the right-angled triangle
  // with the right angle in the lower right
  private static void printLRT(int size) {
    for (int i = 0; i < size; i++) {
      for (int j = 1; size - i > j; j++)
        System.out.print(" ");
      for (int j = 0; j <= i; j++)
        System.out.print("*");
      System.out.println();
    }
  }

  // This method prints out the diamond shape
  private static void printDiamond(int size) {
    int lineNum = 0;
    int toPrint = -1;
    for (int i = (size - 1) / 2; i > 0; i--) { // Upper half of the diamond
      for (int j = 0; j < i; j++)
        System.out.print(" ");
      lineNum += 1;
      if (lineNum - 1 <= (size + 1) / 2) {
        toPrint += 2;
        for (int k = 0; k < toPrint; k++)
          System.out.print("*");
        System.out.println();
      }
    }
    for (int i = 0; i < size; i++) // Longest line
      System.out.print("*");
    System.out.println();
    lineNum += 1;
    toPrint += 2;

    for (int i = 1; i - 1 < (size - 1) / 2; i++) { // lower half of the diamond, ik, ik it's spaghetti code
      for (int j = 0; j < i; j++)
        System.out.print(" ");
      lineNum -= 1;
      toPrint -= 2;
      for (int k = 0; k < toPrint; k++)
        System.out.print("*");
      System.out.println();

    }

  }

  // main method is the starting point of a program
  // "String[] args" carries the arguments passed to the method
  // We will study them in details later
  public static void main(String[] args) {
    int choice = 4;
    int size = 16;
    Scanner scan = new Scanner(System.in);

    printMenu();

    while (choice > 3 | choice < 0) {
      System.out.print("Enter the choice of your shape:");
      choice = scan.nextInt();
    }
    while ((size > 15 | size < 0) | (choice == 3 && (size % 2) == 0)) {
      System.out.print("Enter the size of your shape:");
      size = scan.nextInt();
    }

    switch (choice) {
      case 0:
        printLLT(size);
        break;
      case 1:
        printULT(size);
        break;
      case 2:
        printLRT(size);
        break;
      case 3:
        printDiamond(size);
        break;
    }

  }
}
