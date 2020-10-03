#ifndef _VECTOR_
#define _VECTOR_

#include <iostream>
#include <cassert>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

class Vector {
private:
  int n;
  double* coeff;

public:
  Vector (int , double = 0);
  Vector (const Vector&);
  ~Vector ();
  Vector& operator=(const Vector&);

  int size () const;
  double& operator () (int);
  const double& operator () (int) const;

  void setVector (int where, double what) {
    assert(0 <= where && where < n);
    coeff[where] = what;
  }
  void scanVector () {
    for (size_t i = 0; i < n; i++) {
      cout << "Vector_" << i << " := ";
      cin >> coeff[i];
    }
    cout << endl;
  }
  void printVector () {
    for (size_t i = 0; i < n; i++) {
      cout << "Vector_" << i << " = " << coeff[i] << endl;
    }
    cout << endl;
  }

  double max () const;
  void sort ();
  void unique ();
  void cut (double Cmin, double Cmax);
};

#endif
