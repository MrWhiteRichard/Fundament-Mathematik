#ifndef _TRIMATRIX_
#define _TRIMATRIX_

#include <cassert>
#include <cmath>

class TriMatrix {
private:
  int n;
  double* coeff;

public:
  TriMatrix (int n = 0, double init = 0);
  //TriMatrix (const TriMatrix&);
  ~TriMatrix ();
  TriMatrix& operator = (const TriMatrix&);

  int size () const;
  const double& operator () (int j, int k) const;
  //double& operator () (int j, int k);
  double norm () const;

  void setMatrix(int j, int k, double input) {
    assert(0 <= k && k <= j && j <= n - 1);
    coeff[j*(j + 1)/2 + k] = input;
  }
};

const TriMatrix operator * (TriMatrix&, TriMatrix&);

#endif
