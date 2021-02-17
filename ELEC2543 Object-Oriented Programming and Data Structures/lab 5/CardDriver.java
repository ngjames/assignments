// DO NOT MODIFY THIS FILE

import java.io.*;

public class CardDriver {

  public static void main(String[] args) throws IOException {

    Card cards[];  // an array of Cards, representing a deck of cards

    // put a copy of each card into cards
    int numCards = Suit.values().length * Rank.values().length;
    cards = new Card[numCards];
    int i = 0;
    for (Suit s : Suit.values())
      for (Rank r : Rank.values())
   	    cards[i++] = new Card(r, s);	


    // randomly draw two cards (the first card is put back to the deck)
    MyRandom rnd = new MyRandom();
    Card c1 = cards[rnd.nextInt(cards.length)-1];
    Card c2 = cards[rnd.nextInt(cards.length)-1];

    System.out.println("Two cards are drawn:");
    System.out.println("c1 = " + c1 + " and c2 = " + c2);

    // compare c1 and c2
    if (c1.compareTo(c2) < 0) {
      System.out.println(c1 + " is smaller than " + c2);
    }
    else if (c1.compareTo(c2) == 0) { 
      System.out.println(c1 + " is the same as " + c2); 
    }
    else {
      System.out.println(c1 + " is larger than " + c2);
    }
  }
}
