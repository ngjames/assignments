import java.util.Scanner;
class beginning{
    public static void main(String[] args) {
        int choice, shapenumber;


        System.out.println("This program prints a shape with a certain size of your choice.");
        System.out.println("You have to select the shape from one of the following:" );
        System.out.println("0 -- right-angled triangle with the right angle in the lower left" );
        System.out.println("1 -- right-angled triangle with the right angle in the upper left" );
        System.out.println("2 -- right-angled triangle with the right angle in the lower right") ;
        System.out.println("3 -- a diamond");
        System.out.println("After selecting the shape, you will be asked to input the size of the shape. For triangles, the size is the width and height of the triangle. This size must not be larger than 15. For diamonds, the size tells the number of * on the longest row. The size must be an odd number not larger than 15.");
        System.out.println("");
        
        Scanner scan = new Scanner(System.in);
        
    }
}