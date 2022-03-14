public class BinarySearch {

  // find target from list[i] to list[j]
  // return null if target not found
  //  YOU MUST USE RECURSION TO IMPLEMENT THIS METHOD
  public static Comparable binSearch(int i, int j, Comparable[] list, Comparable target) {
    int mid = (i + j) / 2;
    if (j-i < 0) {
      return null;
    }

    if (!list[mid].equals(target)) {
      if (list[mid].compareTo(target) > 0) {
        return binSearch(i, mid-1, list, target);
      } else {
        return binSearch(mid+1, j, list, target);
      }
    } else {
      return 1;
    }
  }


  // find target from list[]
  // return null if target not found
  public static Comparable search(Comparable[] list, Comparable target) {

    // search the item using method binSearch
    return binSearch(0, list.length-1, list, target);
  }
}
