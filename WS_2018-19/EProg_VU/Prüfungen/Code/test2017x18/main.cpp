#include "vector.cpp"
#include <iostream>
#include <cstdio>

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char const *argv[]) {
  int n = 7;
  double real;
  double imag;
  Vector x(n);

  for (size_t i = 0; i < n; i++) {
    printf("Re_x_%d := ", i);
    cin >> real;
    printf("Im_x_%d := ", i);
    cin >> imag;
    Complex tmp(real, imag);
    x.setEntry(i, tmp);
    cout << endl;
  }
  cout << endl;

  for (size_t i = 0; i < n; i++) {
    printf("x_%d = ", i);
    cout << x(i) << endl;
  }
  cout << endl;

  cout << "This is now the vector, sorted:" << endl << endl;
  x.sort();

  for (size_t i = 0; i < n; i++) {
    printf("x_%d = ", i);
    cout << x(i) << endl;
  }
  cout << endl;

  return 0;
}
