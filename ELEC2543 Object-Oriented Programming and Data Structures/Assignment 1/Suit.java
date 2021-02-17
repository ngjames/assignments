

public enum Suit {
    SPADE("S"),
    HEART("H"),
    CLUB("C"),
    DIAMOND("D");


    private String suit;
    //Constructor
    Suit (String s) {
        suit = s;
    }

    public String toString() {
        return suit;
    }
}
