Game::Game (int dim, bool computer) {
  Board C (dim);
  B = C;

  Player player_1 ("player_1", 1);
  Player player_2 ("player_2", -1);
  player_X = player_1;
  player_O = player_2;

  this->computer    = computer;
  this->turn        = 1;
  this->first_point = 0;
}

string Game::getName (int id) {
  assert(id == 1 || id == -1);
  if (id ==  1) { return player_X.Name(); }
  if (id == -1) { return player_O.Name(); }
}

#include "updateScore.cpp"

double Game::gameStatus () {
  int vector_length = B.getVectorLength( B.getDim() );
  int amount_of_zeros = 0;

  for (size_t i = 0; i < vector_length; i++) {
    if (B[i] == 0) {
      amount_of_zeros++;
    }
  }

  return 1 - (double) amount_of_zeros / vector_length;
}

bool Game::makeTurn () {
  if (computer) { banner("SINGLE PLAYER"); }
  else { banner("MULTI PLAYER"); }

  cout << "Current board:" << endl;
  cout << endl;
  cout << B;

  cout << "Game Status: " << gameStatus() << "%" << endl;
  cout << endl;

  cout << getName( 1) << "'s points:" << endl;
  cout << player_X.Points() << endl;
  cout << getName(-1) << "'s points:" << endl;
  cout << player_O.Points() << endl;
  cout << endl;

  int i = 0, j = 0, k = 0, l = 0;
  cout << "It's " << getName(turn) << "'s turn:" << endl;

  if (getName(turn) != "Computer") {
    if (B.getDim() >= 1) { cout << "i := "; cin >> i; i = abs(i)%3; }
    if (B.getDim() >= 2) { cout << "j := "; cin >> j; j = abs(j)%3; }
    if (B.getDim() >= 3) { cout << "k := "; cin >> k; k = abs(k)%3; }
    if (B.getDim() >= 4) { cout << "l := "; cin >> l; l = abs(l)%3; }
  }
  else {
    do {
      if (B.getDim() >= 1) { i = random(1, 100); i = abs(i)%3; }
      if (B.getDim() >= 2) { j = random(1, 100); j = abs(j)%3; }
      if (B.getDim() >= 3) { k = random(1, 100); k = abs(k)%3; }
      if (B.getDim() >= 4) { l = random(1, 100); l = abs(l)%3; }
    } while(B(i, j, k, l) != 0);

    if (B.getDim() >= 1) { cout << "i := " << i << endl; }
    if (B.getDim() >= 2) { cout << "j := " << j << endl; }
    if (B.getDim() >= 3) { cout << "k := " << k << endl; }
    if (B.getDim() >= 4) { cout << "l := " << l << endl; }
  }
  cout << endl;

  if (B(i, j, k, l) != 0) { makeTurn(); }
  else {
    B(i, j, k, l) = turn;

    printf("Now, there's an '%c' at (", XO(turn) );
    if (B.getDim() >= 1) { cout << i; }
    if (B.getDim() >= 2) { cout << ", " << j; }
    if (B.getDim() >= 3) { cout << ", " << k; }
    if (B.getDim() >= 4) { cout << ", " << l; }
    cout << ")." << endl;

    cout << endl << B;

    updateScore(i, j, k, l);
    switchTurn();

    int ok;
    cout << "Would you like to continue? (1 ~ Yes) ... ";
    cin >> ok;
    cout << endl;

    if (ok != 1) { return false; }
    else { return true; }
  }
}

void Game::switchTurn () { turn *= -1; }

bool Game::gameOver () {
  if ( !(B.getDim() == 2 && first_point != 0) ) {
    int length = B.getVectorLength( B.getDim() );
    for (size_t i = 0; i < length; i++) {
      if (B[i] == 0) {
        return false;
      }
    }
  }

  int winner = first_point;
  if ( player_X.Points() < player_O.Points() ) { winner = -1; }
  if ( player_O.Points() < player_X.Points() ) { winner = 1; }

  if (computer) { banner("SINGLE PLAYER"); }
  else { banner("MULTI PLAYER"); }
  if (winner == 0) { cout << "Draw!!!" << endl; }
  else { cout << getName(winner) << " wins the game!!!" << endl; }
  cout << endl;

  return true;
}
