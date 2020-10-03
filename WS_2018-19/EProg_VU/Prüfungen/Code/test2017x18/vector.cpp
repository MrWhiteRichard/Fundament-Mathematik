#include "vector.hpp"

Vector::Vector (int n) {
  assert(n >= 0);

  this->n = n;

  if (n == 0) { entry = NULL; }
  else { entry = new Complex[n]; }
}

Vector::~Vector () { delete[] entry; }

Complex Vector::operator () (int where) const {
  assert(0 <= where && where < n);
  return entry[where];
}

const Vector& Vector::operator = (const Vector& input) {
  if (this != &input) {
    n = input.size();
    delete[] entry;

    if (n == 0) { entry = NULL; }
    else { entry = new Complex[n]; }

    for (size_t i = 0; i < n; i++) { entry[i] = input(i); }
  }

  return *this;
}

int Vector::find (const Complex& z) const {
  double tmp[n];
  double real;
  double imag;

  for (size_t i = 0; i < n; i++) {
    real = entry[i].real() - z.real();
    imag = entry[i].imag() - z.imag();
    tmp[i] = sqrt(real*real + imag*imag);
  }

  double min = tmp[n - 1];
  int index = n - 1;

  for (int i = n - 1; i >= 0; i--) {
    if (min > tmp[i]) {
      min = tmp[i];
      index = i;
    }
  }

  return index;
}


void Vector::sort () {
  Complex tmp;

  for (size_t i = 0; i < n - 1; i++) {
    for (size_t j = 0; j < n - 1 - i; j++) {
      if (entry[j + 1] < entry[j]) {
        tmp = entry[j];
        entry[j] = entry[j + 1];
        entry[j + 1] = tmp;
      }
    }
  }
}
