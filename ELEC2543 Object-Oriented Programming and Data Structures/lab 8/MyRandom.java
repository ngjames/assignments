// YOU CANNOT MODIFY THIS FILE

import java.util.Random;

public class MyRandom {
  
  Random rnd;

  public MyRandom() {
    rnd = new Random();
  }

  // generate a random integer from 1 to max
  public int nextInt(int max) {
    return rnd.nextInt(max) + 1;
  }
}
