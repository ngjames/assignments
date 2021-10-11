public class Card {
    public Rank rank;
    public Suit suit;

    public Card(Rank rank, Suit suit) {
        this.rank = rank;
        this.suit = suit;
    }


    public String toString() {
        return suit.toString() + rank.toString();
    }

    public int compareTo(Card c) {
        if (c.rank.ordinal() < rank.ordinal()) {
            return 1;
        } else if ((c.rank.ordinal() == rank.ordinal())&& c.suit.ordinal() < suit.ordinal()) {
            return 1;
        } else if ((c.rank.ordinal() == rank.ordinal())&& c.suit.ordinal() == suit.ordinal()) {
            return 0;
        } else {
            return -1;
        }
        
 
        }
        
    }
