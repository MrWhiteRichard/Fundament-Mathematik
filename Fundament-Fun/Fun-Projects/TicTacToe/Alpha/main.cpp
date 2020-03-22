#include "TicTacToe.cpp"

void menu ();
void singlePlayer ();
void multiPlayer ();
void tutorial ();

int main(int argc, char const *argv[]) {
  menu();
  return 0;
}

void menu () {
  banner("TicTacToe ... Multi-Dimensional!!! ");

  cout << endl;
  cout << "[--------]              [--------]                    [--------]                    " << endl;
  cout << "    ||                      ||                            ||                ['''''']" << endl;
  cout << "    ||      ()              ||                            ||                []      " << endl;
  cout << "    ||           _''''      ||       _''''_    _''''      ||       _''''_   [----]  " << endl;
  cout << "    ||      II  |           ||      |  []  |  |           ||      |  []  |  []      " << endl;
  cout << "    ||      II   L____      ||       L_____]   L____      ||       L____l   [______]" << endl;
  cout << endl;

  cout << endl;
  cout << "1. Single Player"  << "        ";
  cout << "2. Multi Player"  << "        ";
  cout << "3. Tutorial"       << "        ";
  cout << "4. Quit Game"      << "        ";
  cout << endl << endl;
  cout << "... ";

  int mode;
  cin >> mode;
  if (mode < 1 || 4 < mode) { menu(); }

  else if (mode == 1) { singlePlayer(); }
  else if (mode == 2) { multiPlayer(); }
  else if (mode == 3) { tutorial(); }
  else { system("clear"); }
}

void singlePlayer () {
  banner("SINGLE PLAYER");

  int dim;
  cout << "In how many dimensions are we playing?" << endl;
  cout << "dim := ";
  cin >> dim;
  if (dim < 1 || 4 < dim) { singlePlayer(); }
  cout << endl;

  Game G (dim, true);

  cout << "Enter your ... " << endl << endl;

  char type;
  do {
    cout << "Player Type: ";
    cin >> type;
  } while(type != 'X' && type != 'O');
  cout << endl;

  string name;
  cout << "Name: ";
  if (type == 'X') {
    cin >> G.player_X.Name();
    if (G.player_X.Name() == "Computer") {
      G.player_X.Name() = "You dare claim my name!?!";
    }
    G.player_O.Name() = "Computer";
  }
  else {
    cin >> G.player_O.Name();
    if (G.player_O.Name() == "Computer") {
      G.player_O.Name() = "You dare claim my name!?!";
    }
    G.player_X.Name() = "Computer";
  }
  cout << endl;

  do {
    if ( !G.makeTurn() ) { break; }
  } while( !G.gameOver() );

  int again;
  cout << "Would you like to play again? (1 ~ Yes) ... ";
  cin >> again;
  if (again == 1) { menu(); }
}

void multiPlayer () {
  banner("MULTI PLAYER");

  int dim;
  cout << "In how many dimensions are we playing?" << endl;
  cout << "dim := ";
  cin >> dim;
  if (dim < 1 || 4 < dim) { multiPlayer(); }
  cout << endl;

  Game G (dim, false);

  cout << "Who's playing? ... " << endl << endl;
  cout << "X: ";
  cin >> G.player_X.Name();
  cout << "O: ";
  cin >> G.player_O.Name();
  cout << endl;

  do {
    if ( !G.makeTurn() ) { break; }
  } while( !G.gameOver() );

  int again;
  cout << "Would you like to play again? (1 ~ Yes) ... ";
  cin >> again;
  if (again == 1) { menu(); }
}

void tutorial () {
  banner("TUTORIAL");

  cout << "The attempt of this game is to generalise the generic, 2-dimensional TicTacToe." << endl;
  cout << "All of this is done, while still allowing the possibility, of embedding the original in the more abstract rule set." << endl;
  cout << endl;

  cout << "The scoring generalisation:" << endl;
  cout << endl;
  cout << "Instead of immediatelly ending the game, once a player encounters a TicTacToe, we let him recieve a point instead." << endl;
  cout << "This will ensure longer playing time, especially in higher dimensions." << endl;
  cout << "Once all fields are taken, the game is over." << endl;
  cout << "The player with the most points winns." << endl;
  cout << "If both players hold an equal amount of points, the one, who scored the first point winns." << endl;
  cout << endl;

  cout << "The board extension:" << endl;
  cout << endl;
  cout << "In order to move from 2 to 3 dimensions, two copies of the board are made and placed beneath one another." << endl;
  cout << "The player may now not only place markers on one, but 3 boards simultaneously." << endl;
  cout << "Alternatively, the board may now be seen as a cube." << endl;
  cout << "Naturally, a TicTacToe can now also occur, after rotating it, or even in the newly occuring 'room diagonals'." << endl;
  cout << "Similarly, we can move from 3 dimensions into a 4 dimensional hypercube." << endl;
  cout << endl;

  cout << "Placing a marker:" << endl;
  cout << endl;
  cout << "Each point on the board is described by 4 values." << endl;
  cout << "Every axis can have the values 0, 1, 2." << endl;
  cout << "To describe a point only as many values, as there are dimensions, are requived." << endl;
  cout << "In the tuple (i, j, k, l), i and j are vertical, while j and l are horizontal." << endl;
  cout << endl;

  cout << "Example board (4 dimensions):" << endl;
  cout << endl;

  Board B_1 (4);
  B_1(0, 0, 2, 2) = 1;
  B_1(1, 0, 2, 2) = 1;
  B_1(2, 0, 2, 2) = 1;
  B_1(0, 0, 0, 2) = -1;
  B_1(0, 1, 0, 2) = -1;
  B_1(0, 2, 0, 2) = -1;
  B_1(0, 0, 0, 0) = 1;
  B_1(0, 0, 1, 0) = 1;
  B_1(0, 0, 2, 0) = 1;
  B_1(2, 0, 1, 0) = -1;
  B_1(2, 0, 1, 1) = -1;
  B_1(2, 0, 1, 2) = -1;
  cout << B_1;

  int play;
  cout << "Would you like to play? (1 ~ Yes) ... ";
  cin >> play;
  if (play == 1) { menu(); }
}
