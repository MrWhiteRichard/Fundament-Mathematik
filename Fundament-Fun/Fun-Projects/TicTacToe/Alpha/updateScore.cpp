void Game::updateScore (int i, int j, int k, int l) {
  int additional = 0;

  int i_0 = (i + 0)%3; int i_1 = (i + 1)%3; int i_2 = (i + 2)%3;
  int j_0 = (j + 0)%3; int j_1 = (j + 1)%3; int j_2 = (j + 2)%3;
  int k_0 = (k + 0)%3; int k_1 = (k + 1)%3; int k_2 = (k + 2)%3;
  int l_0 = (l + 0)%3; int l_1 = (l + 1)%3; int l_2 = (l + 2)%3;

/*
cout << "i_0 = " << i_0 << endl;
cout << "i_1 = " << i_1 << endl;
cout << "i_2 = " << i_2 << endl;
cout << endl;
cout << "j_0 = " << j_0 << endl;
cout << "j_1 = " << j_1 << endl;
cout << "j_2 = " << j_2 << endl;
cout << endl;
cout << "k_0 = " << k_0 << endl;
cout << "k_1 = " << k_1 << endl;
cout << "k_2 = " << k_2 << endl;
cout << endl;
cout << "l_0 = " << l_0 << endl;
cout << "l_1 = " << l_1 << endl;
cout << "l_2 = " << l_2 << endl;
cout << endl;
*/

if (B.getDim() >= 1) {

// 1.0
additional += TicTacToe( B(i_0, j, k, l), B(i_1, j, k, l), B(i_2, j, k, l) );
/*
printf("B(i_0, j, k, l) = %d\n", B(i_0, j, k, l) );
printf("B(i_1, j, k, l) = %d\n", B(i_1, j, k, l) );
printf("B(i_2, j, k, l) = %d\n", B(i_2, j, k, l) );
*/

/*
x
x
x
*/

}

if (B.getDim() >= 2) {

// 2.0
additional += TicTacToe( B(i, j_0, k, l), B(i, j_1, k, l), B(i, j_2, k, l) );

/*
x x x
- - -
- - -
*/

// 2.1.1a
if (i == j) {
	additional += TicTacToe( B(i_0, j_0, k, l), B(i_1, j_1, k, l), B(i_2, j_2, k, l) );
}

/*
x - -
- x -
- - x
*/

// 2.1.1b
if (2 - i == j) {
	additional += TicTacToe( B(i_0, j_0, k, l), B(i_1, j_2, k, l), B(i_2, j_1, k, l) );
}

/*
- - x
- x -
x - -
*/

}

if (B.getDim() >= 3) {

// 3.0
additional += TicTacToe( B(i, j, k_0, l), B(i, j, k_1, l), B(i, j, k_2, l) );

/*
x - -
- - -
- - -

x - -
- - -
- - -

x - -
- - -
- - -
*/

// 3.1.1a
if (i == k) {
	additional += TicTacToe( B(i_0, j, k_0, l), B(i_1, j, k_1, l), B(i_2, j, k_2, l) );
}

/*
x - -
- - -
- - -

- - -
x - -
- - -

- - -
- - -
x - -
*/

// 3.1.1b
if (2 - i == k) {
	additional += TicTacToe( B(i_0, j, k_0, l), B(i_1, j, k_2, l), B(i_2, j, k_1, l) );
}

/*
- - -
- - -
x - -

- - -
x - -
- - -

x - -
- - -
- - -
*/

// 3.1.2a
if (j == k) {
	additional += TicTacToe( B(i, j_0, k_0, l), B(i, j_1, k_1, l), B(i, j_2, k_2, l) );
}

/*
x - -
- - -
- - -

- x -
- - -
- - -

- - x
- - -
- - -
*/

// 3.1.2b
if (2 - j == k) {
	additional += TicTacToe( B(i, j_0, k_0, l), B(i, j_1, k_2, l), B(i, j_2, k_1, l) );
}

/*
- - x
- - -
- - -

- x -
- - -
- - -

x - -
- - -
- - -
*/

// 3.2.1a.1a
if (i == j) {
	if (j == k) {
		additional += TicTacToe( B(i_0, j_0, k_0, l), B(i_1, j_1, k_1, l), B(i_2, j_2, k_2, l) );
	}
}

/*
x - -
- - -
- - -

- - -
- x -
- - -

- - -
- - -
- - x
*/

// 3.2.1a.1b
if (i == j) {
	if (2 - j == k) {
		additional += TicTacToe( B(i_0, j_0, k_0, l), B(i_1, j_1, k_2, l), B(i_2, j_2, k_1, l) );
	}
}

/*
- - -
- - -
- - x

- - -
- x -
- - -

x - -
- - -
- - -
*/

// 3.2.1b.1a
if (2 - i == j) {
	if (j == k) {
		additional += TicTacToe( B(i_0, j_0, k_0, l), B(i_1, j_2, k_2, l), B(i_2, j_1, k_1, l) );
	}
}

/*
- - -
- - -
x - -

- - -
- x -
- - -

- - x
- - -
- - -
*/

// 3.2.1b.1b
if (2 - i == j) {
	if (2 - j == k) {
		additional += TicTacToe( B(i_0, j_0, k_0, l), B(i_1, j_2, k_1, l), B(i_2, j_1, k_2, l) );
	}
}

/*
- - x
- - -
- - -

- - -
- x -
- - -

- - -
- - -
x - -
*/

}

if (B.getDim() >= 4) {

// 4.0
additional += TicTacToe( B(i, j, k, l_0), B(i, j, k, l_1), B(i, j, k, l_2) );

/*
x - -   x - -   x - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.1.3a
if (i == l) {
	additional += TicTacToe( B(i_0, j, k, l_0), B(i_1, j, k, l_1), B(i_2, j, k, l_2) );
}

/*
x - -   - - -   - - -
- - -   x - -   - - -
- - -   - - -   x - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.1.3b
if (2 - i == l) {
	additional += TicTacToe( B(i_0, j, k, l_0), B(i_1, j, k, l_2), B(i_2, j, k, l_1) );
}

/*
- - -   - - -   x - -
- - -   x - -   - - -
x - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.1.2a
if (j == l) {
	additional += TicTacToe( B(i, j_0, k, l_0), B(i, j_1, k, l_1), B(i, j_2, k, l_2) );
}

/*
x - -   - x -   - - x
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.1.2b
if (2 - j == l) {
	additional += TicTacToe( B(i, j_0, k, l_0), B(i, j_1, k, l_2), B(i, j_2, k, l_1) );
}

/*
- - x   - x -   x - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.1.1a
if (k == l) {
	additional += TicTacToe( B(i, j, k_0, l_0), B(i, j, k_1, l_1), B(i, j, k_2, l_2) );
}

/*
x - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   x - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   x - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.1.1b
if (2 - k == l) {
	additional += TicTacToe( B(i, j, k_0, l_0), B(i, j, k_1, l_1), B(i, j, k_2, l_2) );
}

/*
- - -   - - -   x - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   x - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

x - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.1a.2a
if (i == j) {
	if (j == l) {
		additional += TicTacToe( B(i_0, j_0, k, l_0), B(i_1, j_1, k, l_1), B(i_2, j_2, k, l_2) );
	}
}

/*
x - -   - - -   - - -
- - -   - x -   - - -
- - -   - - -   - - x

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.1a.2b
if (i == j) {
	if (2 - j == l) {
		additional += TicTacToe( B(i_0, j_0, k, l_0), B(i_1, j_1, k, l_2), B(i_2, j_2, k, l_1) );
	}
}

/*
- - -   - - -   x - -
- - -   - x -   - - -
- - x   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.1b.2a
if (2 - i == j) {
	if (j == l) {
		additional += TicTacToe( B(i_0, j_0, k, l_0), B(i_1, j_2, k, l_2), B(i_2, j_1, k, l_1) );
	}
}

/*
- - -   - - -   - - x
- - -   - x -   - - -
x - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.1b.2b
if (2 - i == j) {
	if (2 - j == l) {
		additional += TicTacToe( B(i_0, j_0, k, l_0), B(i_1, j_2, k, l_1), B(i_2, j_1, k, l_2) );
	}
}

/*
- - x   - - -   - - -
- - -   - x -   - - -
- - -   - - -   x - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.2a.1a
if (i == k) {
	if (k == l) {
		additional += TicTacToe( B(i_0, j, k_0, l_0), B(i_1, j, k_1, l_1), B(i_2, j, k_2, l_2) );
	}
}

/*
x - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   x - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   x - -
*/

// 4.2.2a.1b
if (i == k) {
	if (2 - k == l) {
		additional += TicTacToe( B(i_0, j, k_0, l_0), B(i_1, j, k_1, l_2), B(i_2, j, k_2, l_1) );
	}
}

/*
- - -   - - -   x - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   x - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
x - -   - - -   - - -
*/

// 4.2.2b.1a
if (2 - i == k) {
	if (k == l) {
		additional += TicTacToe( B(i_0, j, k_0, l_0), B(i_1, j, k_2, l_2), B(i_2, j, k_1, l_1) );
	}
}

/*
- - -   - - -   - - -
- - -   - - -   - - -
x - -   - - -   - - -

- - -   - - -   - - -
- - -   x - -   - - -
- - -   - - -   - - -

- - -   - - -   x - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.2b.1b
if (2 - i == k) {
	if (2 - k == l) {
		additional += TicTacToe( B(i_0, j, k_0, l_0), B(i_1, j, k_2, l_2), B(i_2, j, k_1, l_1) );
	}
}

/*
- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   x - -

- - -   - - -   - - -
- - -   x - -   - - -
- - -   - - -   - - -

x - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.1a.1a
if (j == k) {
	if (k == l) {
		additional += TicTacToe( B(i, j_0, k_0, l_0), B(i, j_1, k_1, l_1), B(i, j_2, k_2, l_2) );
	}
}

/*
x - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - x -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - x
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.1a.1b
if (j == k) {
	if (2 - k == l) {
		additional += TicTacToe( B(i, j_0, k_0, l_0), B(i, j_1, k_1, l_2), B(i, j_2, k_2, l_1) );
	}
}

/*
- - -   - - -   x - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - x -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - x   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.1b.1a
if(2 - j == k) {
	if(k == l) {
		additional += TicTacToe( B(i, j_0, k_0, l_0), B(i, j_1, k_2, l_2), B(i, j_2, k_1, l_1) );
	}
}

/*
- - x   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - x -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   x - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.2.1b.1b
if(2 - j == k) {
	if(2 - k == l) {
		additional += TicTacToe( B(i, j_0, k_0, l_0), B(i, j_1, k_2, l_1), B(i, j_2, k_1, l_2) );
	}
}

/*
- - -   - - -   - - x
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - x -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

x - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.3.1a.1a.1a
if (i == j) {
	if (j == k) {
		if (k == l) {
			additional += TicTacToe( B(i_0, j_0, k_0, l_0), B(i_1, j_1, k_1, l_1), B(i_2, j_2, k_2, l_2) );
		}
	}
}

/*
x - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - x -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - x
*/

// 4.3.1a.1a.1b
if (i == j) {
	if (j == k) {
		if (2 - k == l) {
			additional += TicTacToe( B(i_0, j_0, k_0, l_0), B(i_1, j_1, k_1, l_2), B(i_2, j_2, k_2, l_1) );
		}
	}
}

/*
- - -   - - -   x - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - x -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - x   - - -   - - -
*/

// 4.3.1a.1b.1a
if (i == j) {
	if (2 - j == k) {
		if (k == l) {
			additional += TicTacToe( B(i_0, j_0, k_0, l_0), B(i_1, j_1, k_2, l_2), B(i_2, j_2, k_1, l_1) );
		}
	}
}

/*
- - -   - - -   - - -
- - -   - - -   - - -
- - x   - - -   - - -

- - -   - - -   - - -
- - -   - x -   - - -
- - -   - - -   - - -

- - -   - - -   x - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.3.1a.1b.1b
if (i == j) {
	if (2 - j == k) {
		if (2 - k == l) {
			additional += TicTacToe( B(i_0, j_0, k_0, l_0), B(i_1, j_1, k_1, l_1), B(i_2, j_2, k_2, l_2) );
		}
	}
}

/*
- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - x

- - -   - - -   - - -
- - -   - x -   - - -
- - -   - - -   - - -

x - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.3.1b.1a.1a
if (2 - i == j) {
	if (j == k) {
		if (k == l) {
			additional += TicTacToe( B(i_0, j_0, k_0, l_0), B(i_1, j_2, k_2, l_2), B(i_2, j_1, k_1, l_1) );
		}
	}
}

/*
- - -   - - -   - - -
- - -   - - -   - - -
x - -   - - -   - - -

- - -   - - -   - - -
- - -   - x -   - - -
- - -   - - -   - - -

- - -   - - -   - - x
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.3.1b.1a.1b
if (2 - i == j) {
	if (j == k) {
		if (2 - k == l) {
			additional += TicTacToe( B(i_0, j_0, k_0, l_0), B(i_1, j_2, k_2, l_1), B(i_2, j_1, k_1, l_2) );
		}
	}
}

/*
- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   x - -

- - -   - - -   - - -
- - -   - x -   - - -
- - -   - - -   - - -

- - x   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -
*/

// 4.3.1b.1b.1a
if (2 - i == j) {
	if (2 - j == k) {
		if (k == l) {
			additional += TicTacToe( B(i_0, j_0, k_0, l_0), B(i_1, j_2, k_1, l_1), B(i_2, j_1, k_2, l_2) );
		}
	}
}

/*
- - x   - - -   - - -
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - x -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
- - -   - - -   x - -
*/

// 4.3.1b.1b.1b
if (2 - i == j) {
	if (2 - j == k) {
		if (2 - k == l) {
			additional += TicTacToe( B(i_0, j_0, k_0, l_0), B(i_1, j_2, k_1, l_2), B(i_2, j_1, k_2, l_1) );
		}
	}
}

/*
- - -   - - -   - - x
- - -   - - -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - x -   - - -
- - -   - - -   - - -

- - -   - - -   - - -
- - -   - - -   - - -
x - -   - - -   - - -
*/

}

if (turn ==  1) {
  player_X.Points() += additional;
  if (first_point == 0 && additional != 0) { first_point = 1; }
  cout << getName( 1);
}
if (turn == -1) {
  player_O.Points() += additional;
  if (first_point == 0 && additional != 0) { first_point = -1; }
  cout << getName(-1);
}
cout << " scored " << additional << " point";
if (additional != 1) { cout << "s"; }
cout << "!" << endl;
cout << endl;

}
