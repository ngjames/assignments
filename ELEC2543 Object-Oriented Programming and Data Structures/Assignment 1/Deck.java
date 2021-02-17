import java.util.*; 
public class Deck {
  static ArrayList<Card> deck = new ArrayList<Card>();
  ArrayList<Card> shuffleTemp1 = new ArrayList<Card>();
  ArrayList<Card> shuffleTemp2 = new ArrayList<Card>();

  public Deck(int n) {
    // init deck
    for (Suit s : Suit.values())
      for (Rank r : Rank.values())
        deck.add(new Card(r, s));

    // shuffling begins here
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < 26; j++) {
        shuffleTemp1.add(deck.remove(0));
      }
      for (int j = 0; j < 26; j++) {
        shuffleTemp2.add(deck.remove(0));
      }
      for (int j = 0; j < 26; j++) {
        deck.add(shuffleTemp1.remove(0));
        deck.add(shuffleTemp2.remove(0));
      }
    }
  }

  public Card drawCard() {
    return deck.remove(0);
  }
}

//Arrays.asList("S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK", "SA", "H2", "H3", "H4","H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK", "HA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK", "CA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK", "DA")