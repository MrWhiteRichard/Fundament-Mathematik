void banner (string Banner) {
  system("clear");
  cout << endl;
  cout << "--------------------------------[ " << Banner << " ]--------------------------------" << endl;
  cout << endl << endl;
}

char XO (int i) {
  assert(i == -1 || i == 0 || i == 1);

  if (i == 1)  { return 'X'; }
  if (i == 0)  { return '-'; }
  if (i == -1) { return 'O'; }
}

int TicTacToe (int a, int b, int c) {
  if (a == b && b == c) { return 1; }
  else { return 0; }
}

int random (int min, int max) {
  static bool first = true;
  if (first) {
    srand( time(NULL) );
    first = false;
  }
  return min + rand() % (( max + 1 ) - min);
}
