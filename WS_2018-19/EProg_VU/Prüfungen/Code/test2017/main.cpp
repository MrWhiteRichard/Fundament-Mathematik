#include "solution.cpp"
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char const *argv[]) {
  int dim = 5;
  double tmp;
  TriMatrix A(dim);
  Vector b(dim, 0, "b");

  for (int i = 0; i < dim; i++) {
    for (int j = i; j < dim; j++) {
      cout << "A_{" << j << ", " << i << "} := ";
      cin >> tmp;
      A.setMatrix(j, i, tmp);
    }
    cout << endl;
  }

  for (int i = 0; i < dim; i++) {
    cout << "b_" << i << " := ";
    cin >> tmp;
    b.setVector(i, tmp);
  }
  cout << endl;

  cout << "A = " << endl << endl;

  for (int i = 0; i < dim; i++) {
    for (int j = 0; j <= i; j++) {
      cout << A(i, j) << " ";
    }
    cout << endl;
  }
  cout << endl;

  cout << "b = " << endl;

  for (int i = 0; i < dim; i++) {
    cout << b(i) << endl;
  }
  cout << endl;

  TriMatrix B = A*A;

  cout << "B = A*A = " << endl << endl;

  for (int i = 0; i < dim; i++) {
    for (int j = 0; j <= i; j++) {
      cout << B(i, j) << " ";
    }
    cout << endl;
  }
  cout << endl;

  Vector x = A|b;
  //x.setName("x");
  cout << "Consider x = A|b = " << endl << endl;

  for (int i = 0; i < dim; i++) {
    cout << x(i) << endl;
  }
  cout << endl;

  return 0;
}
