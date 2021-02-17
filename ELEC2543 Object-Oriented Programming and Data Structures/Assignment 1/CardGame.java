public class CardGame {

  // YOU CANNOT DEFINE OTHER INSTANCE VARIABLES
  private Player[] players;	// players in this game
  private int numRounds;	// number of rounds in this game
  private Deck deck;		// deck of cards

  // constructor
  // YOU SHOULD NOT MODIFY THIS METHOD
  public CardGame(Player[] players) {
    
    this.players = players;
    deck = new Deck(5);

  }

  // implement this method
  public void play() {
    
    // find out the number of rounds in this game
    numRounds = 52 / players.length;

    // distribute cards among players
    for (int i = 0; i <numRounds; i++) {
      for (Player j : players) {
        j.addCard(deck.drawCard());
      }
    }
    // develop the loop for each round
    // (1) print out the cards each player has
    // (2) print out the cards each player plays
    // (3) identify the winner of this round
    for (int i = 0; i <numRounds; i++) {

      for (Player p : players) {
        p.printHand();
      }
      Card cardCache1, cardCache2;
      Boolean first = true;
      Player winningPlayer = players[0];
      cardCache1 = new Card(Rank.TWO, Suit.SPADE);
      for (Player p : players) {
        if (first) {
          cardCache2 = p.playCard();
          cardCache1 = cardCache2;
          first = false;
        } else {
          cardCache2 = p.playCard();
        }
        System.out.println(p.getName() + " plays " + cardCache2);
        if (cardCache2.compareTo(cardCache1) == 1) {
          cardCache1 = cardCache2;
          winningPlayer = p;
        }
      }
      System.out.println("The winner of this round is "+ winningPlayer.getName()+ ".");
      first = true;
      System.out.println();
      
    }
  }
}
