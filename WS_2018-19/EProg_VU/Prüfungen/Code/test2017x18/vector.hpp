#ifndef _VECTOR_
#define _VECTOR_

#include "complex.cpp"

class Vector {
private:
  int n;
  Complex* entry;

public:
  Vector (int n = 0);
  ~Vector ();
  Vector (const Vector&);
  const Vector& operator = (const Vector&);

  //const Complex& operator () (int) const;
  Complex operator () (int) const;
  int size () const { return n; }
  int find (const Complex& z) const;
  void sort ();

  Complex getEntry (int i) { return entry[i]; }
  void setEntry (int where, const Complex& what) { entry[where] = what; }
};

#endif
