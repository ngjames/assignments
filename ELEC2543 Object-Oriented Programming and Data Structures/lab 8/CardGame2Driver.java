import java.io.*;

public class CardGame2Driver {

  public static void main(String[] args) throws IOException {

    Player[] players = InitializePlayer.getPlayers();
    CardGame2 game = new CardGame2(players);
    game.play();
  }
}
