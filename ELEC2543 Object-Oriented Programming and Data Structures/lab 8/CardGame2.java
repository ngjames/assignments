public class CardGame2 {

  private Player[] players;	// players in this game

  // constructor
  public CardGame2(Player[] players) {
    this.players = players;
  }

  public void play() {
    int gameLength = players[0].cards.size();
    for (int i = 0; i < gameLength; i++) {
      for (Player p : players) {
        p.printHand();
      }
      int WinnerPos = 0;
      Card LargestCard = new Card(Rank.TWO, Suit.SPADE);
      Card PlayedCard;
      
      for (int j = 0; j < players.length; j++) {
        if (j == 0) {
          WinnerPos = 0;
          PlayedCard = players[j].playCard();
          LargestCard = PlayedCard;

        } else {
          PlayedCard = players[j].playCard();
          
          if (PlayedCard.compareTo(LargestCard) > 0) {
            WinnerPos = j;
            LargestCard = PlayedCard;
          }
        }
        System.out.println(players[j].getName()+ " plays " + PlayedCard.toString());
      }
    System.out.println("The winner of this round is " + players[WinnerPos].getName() + ".");
    System.out.println("");
    }
  }
}
