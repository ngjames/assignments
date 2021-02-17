public class RandomWalkGame {

  // PUT IN APPROPRIATE VISIBILITY MODIFIERS
  private int length;
  private int playerPos;

  public RandomWalkGame(int length) {
     this.length = length;
     this.playerPos = 1;
  }


  // YOU SHOULD NOT MODIFY THIS METHOD EXCEPT 
  // PUTTING IN APPROPRIATE VISIBILITY MODIFIER
  public void printMap() {

    for (int i = 1; i < playerPos; i++)
      System.out.print(".");

    System.out.print('P');

    for (int i = playerPos+1; i <= length; i++)
      System.out.print(".");
  }
  
  // IMPLEMENT THE FOLLOWING METHOD
  public void play() {
 
    // create an appropriate MyDie object for
    // generating the distance
    MyDie distDie = new MyDie(1, 3);

    boolean gameEnd = false;

    int distance;  // distance that the player is going to move

    int numRound = 0;

    while (!gameEnd) {

      printMap();

      // use distDie to generate how many units the player is advancing
      distance = distDie.roll();

      // compute the new position if the move is made
      // and determine whether the game ends
      if ((distance + playerPos) > length) {
        playerPos = length - (distance - (length - playerPos));
      } else if ((distance + playerPos) < length) {
        playerPos = playerPos + distance;
      } else {
        playerPos = distance;
        gameEnd = true;
      }

      


      // print out the distance the player moves
      System.out.println("\t[Player moves " + distance + " unit(s)]");

      numRound++;
    }

    System.out.println("The game ends after " + numRound + " rounds.");
  }
}
