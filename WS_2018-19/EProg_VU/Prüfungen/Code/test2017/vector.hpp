#ifndef _VECTOR_
#define _VECTOR_

#include <cassert>
#include <string>

class Vector {
private:
  std::string name;
  int n;
  double* coeff;

public:
  Vector (int n = 0, double init = 0, std::string name = "Hans");
  Vector (const Vector&);
  ~Vector ();
  Vector& operator = (const Vector &);

  std::string getName () const { return name; }
  void setName (std::string name) { this->name = name; }
  int size () const;
  const double& operator () (int j) const;
  double& operator () (int j);

  void setVector (int j, double input) {
    assert(0 <= j && j <= n);
    coeff[j] = input;
  }
};

#endif
