#ifndef _POLYNOMIAL_
#define _POLYNOMIAL_

#include <cmath>
#include <cassert>

class Polynomial {
private:
  int n;

public:
  double* a;
  Polynomial (int n = 0);
  Polynomial (const Polynomial&);
  ~Polynomial ();
  Polynomial& operator = (const Polynomial &);

  int degree () const;
  Polynomial diff () const;
  double operator () (double x) const;
  const double& operator [] (int j) const;
  double& operator [] (int j);
};

#endif
