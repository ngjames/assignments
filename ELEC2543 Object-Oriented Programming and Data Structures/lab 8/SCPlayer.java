public class SCPlayer extends Player {

    public SCPlayer(String name) {
        super(name);
    }

    public Card playCard() {
        if (cards.size() == 0) return null;
        return cards.remove(0);
    }
}