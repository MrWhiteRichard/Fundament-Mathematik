#ifndef _TICTACTOE_
#define _TICTACTOE_

#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cassert>

class Player {
private:
  std::string name;
  int id;
  int points;

public:
  Player (std::string = "player", int = 1, int = 0);
  Player (const Player&);
  Player& operator = (const Player&);
  ~Player ();

  std::string& Name () { return name; }
  int& ID () { return id; }
  int& Points () { return points; }

  const std::string& Name () const { return name; }
  const int& ID () const { return id; }
  const int& Points () const { return points; }
};

class Board {
private:
  int dim;
  int* coeff;

public:
  Board (int = 4);
  Board (const Board&);
  Board& operator = (const Board&);
  ~Board ();

  const int& getDim () const;
  const int getVectorLength (int) const;

  int& operator [] (int);
  const int& operator [] (int) const;
  int& operator () (int = 0, int = 0, int = 0, int = 0);
  const int& operator () (int = 0, int = 0, int = 0, int = 0) const;
};

class Game {
private:
  int first_point;
  bool computer;
  int turn;

public:
  Board B;
  Player player_X;
  Player player_O;

  Game (int, bool);

  double gameStatus ();
  std::string getName (int);
  void updateScore (int, int, int, int);
  bool makeTurn ();
  void switchTurn ();
  bool gameOver ();
};

#endif
