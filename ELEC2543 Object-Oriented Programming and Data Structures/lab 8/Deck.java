// YOU CANNOT MODIFY THIS FILE

import java.util.ArrayList;

public class Deck {
  private ArrayList<Card> cards;
  private static MyRandom rnd = new MyRandom(); 

  public Deck() {
    cards = new ArrayList<Card>();
    for (Suit s : Suit.values())
      for (Rank r : Rank.values())
        cards.add(new Card(r, s));
  }

  public boolean isEmpty() {
    return (cards.size() == 0);
  }

  public Card drawCard() {
    if (isEmpty()) return null;

    int pos = rnd.nextInt(cards.size()) - 1;
    return cards.remove(pos);
  }
}
