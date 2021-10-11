public class FindLargest {
    
    public static Comparable findLargest(Comparable[] arr) {
        if (arr.length == 0) {
            return null;
        } else {
            Comparable largest = arr[0];
            for (int i = 1; i < arr.length; i++) {
                if (largest.compareTo(arr[i]) == -1) {
                    largest = arr[i];
                }
            }
            return largest;
        }
    }
}
