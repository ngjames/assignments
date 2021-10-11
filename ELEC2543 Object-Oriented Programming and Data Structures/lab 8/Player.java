import java.util.ArrayList;

public class Player {

  // NO MORE INSTANCE VARIABLE CAN BE DEFINED
  private String name;  // name of the player
  public ArrayList<Card> cards; // cards the player has
  private static MyRandom rnd = new MyRandom();

  // YOU CANNOT MODIFY THIS FUNCTION
  public Player(String name) {
    this.name = name;
    cards = new ArrayList<Card>();
  }

  // YOU CANNOT MODIFY THIS FUNCTION
  public String getName() {
    return name;
  }

  // cards are ordered from small to large
  public void addCard(Card card) {
    if (cards.size() != 0) {
      boolean notInserted = true;
      for (int i = 0; i < cards.size(); i++) {
        if (notInserted) {
          if (cards.get(i).compareTo(card) > 0) {
            cards.add(i, card);
            notInserted = false;  
          }
        }
      }
      if (notInserted) {
        cards.add(card);
      }
    } else {
      cards.add(card);
    }
  }

  // YOU CANNOT MODIFY THIS FUNCTION
  public Card playCard() {
    if (cards.size() == 0) return null;

    return cards.remove(rnd.nextInt(cards.size())-1);
  }

  // YOU CANNOT MODIFY THIS FUNCTION
  public void printHand() {
    System.out.print(name);
    System.out.println(" has cards: " + cards);
  }
}
