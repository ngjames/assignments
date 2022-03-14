public class PascalTriangle {

  public static int[] computePT(int k) {

    int[] soln = new int[k];
    if (k == 1) {
      soln[0] = 1;
      return soln; 
    }
    else {
      int[] prev = computePT(k-1);
      for (int i = 0; i < k; i++) {
        try {
          soln[i] = prev[i-1] + prev[i];

        } catch (Exception e) {
          soln[i] = 1;
      }
      };
      return soln;
    }
  }
}