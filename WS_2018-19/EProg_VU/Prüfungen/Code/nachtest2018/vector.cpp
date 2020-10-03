#include "vector.hpp"

Vector::Vector (int dim, double init) {
  assert(dim >= 0);
  n = dim;

  if (n == 0) { coeff = NULL; }
  else {
    coeff = new double[n];
    for (size_t i = 0; i < n; i++) { coeff[i] = init; }
  }
}

Vector::~Vector () {
  delete[] coeff;
  coeff = NULL;
}

Vector& Vector::operator = (const Vector& input) {
  if (this != &input) {
    delete[] coeff;
    n = input.size();
    coeff = new double[n];
    for (size_t i = 0; i < n; i++) { coeff[i] = input(i); }
  }
  return *this;
}

int Vector::size () const { return n; }

double& Vector::operator () (int i) {
  assert(0 <= i && i < n);
  return coeff[i];
}

const double& Vector::operator () (int i) const {
  assert(0 <= i && i < n);
  return coeff[i];
}

double Vector::max () const {
  assert(n > 0);
  double max = coeff[0];

  for (size_t i = 1; i < n; i++) {
    if (max < coeff[i]) {
      max = coeff[i];
    }
  }

  return max;
}

void Vector::sort () {
  double tmp;

  for (size_t i = 0; i < n - 1; i++) {
    for (size_t j = 0; j < n - 1 - i; j++) {
      if (coeff[j] > coeff[j + 1]) {
        tmp = coeff[j];
        coeff[j] = coeff[j + 1];
        coeff[j + 1] = tmp;
      }
    }
  }
}

void Vector::unique () {
  if (n > 0) {
    sort();
    int count = 1;
    int tracker = 1;

    for (size_t i = 0; i < n - 1; i++) {
      if (coeff[i] != coeff[i + 1]) {
        count++;
      }
    }

    Vector tmp(count);
    tmp.setVector(0, coeff[0]);

    for (size_t i = 0; i < n - 1; i++) {
      if (coeff[i] != coeff[i + 1]) {
        tmp.setVector(tracker, coeff[i + 1]);
        tracker++;
      }
    }

    *this = tmp;
  }
}


void Vector::cut (double Cmin, double Cmax) {
  if (n > 0) {
    int count = 0;
    int tracker = 0;

    for (size_t i = 0; i < n; i++) {
      if (Cmin <= coeff[i] && coeff[i] <= Cmax) {
        count++;
      }
    }

    Vector tmp(count);

    for (size_t i = 0; i < n; i++) {
      if (Cmin <= coeff[i] && coeff[i] <= Cmax) {
        tmp.setVector(tracker, coeff[i]);
        tracker++;
      }
    }

    *this = tmp;
  }
}

Vector eratosthenes (int n) {
  assert(n >= 2);

  Vector x(n);
  for (size_t i = 0; i < n; i++) { x.setVector(i, i + 1); }

  for (size_t i = 1; i < n; i++) {
    if ( fabs( x(i) ) > 1e-15 ) {
      for (size_t j = i + 1; j < n; j++) {
        if ( (int) x(j) % (int) x(i) == 0 && fabs( x(j) ) > 1e-15 ) {
          x.setVector(j, 0);
        }
      }
    }
  }

  x.cut(2, n);
  return x;
}

Vector foo (int n) {
  Vector x = eratosthenes(n);
  Vector y( x. size() );
  for (int j = 0; j < x.size(); ++j) {
    while (n / (int) x(j)*x(j) == n) {
      n = n/x(j);
      y(j) = y(j) + 1;
      cout << n << " : ";
      for (int k = 0; k < x.size(); ++k) {
        cout << " " << y(k);
      }
      cout << endl ;
    }
  }
  return y;
}
