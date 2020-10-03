#include "vector.hpp"
#include <iostream>

using std::string;

Vector::Vector (int n, double init, string name) {
  assert(n >= 0);
  this->n = n;
  this->name = name;

  if (n == 0) { coeff = NULL; }
  else { coeff = new double[n]; }

  for (int i = 0; i < n; i++) { coeff[i] = init; }
}

Vector::Vector (const Vector& rhs) {
  n = rhs.size();
  name = rhs.getName();
  coeff = new double[n];

  for (size_t i = 0; i < n; i++) { coeff[i] = rhs(i); }
}

Vector::~Vector () {
  delete[] coeff;
  std::cout << "Destruktor von " << name << "!!!" << std::endl;
}

Vector& Vector::operator = (const Vector & rhs) {
  if (this != &rhs) {
    n = rhs.size();
    name = rhs.getName();
    delete[] coeff;
    coeff = new double[n];

    for (int i = 0; i < n; i++) { coeff[i] = rhs(i); }
  }

  return *this;
}

int Vector::size () const { return n; }

const double& Vector::operator () (int j) const {
  assert(0 <= j && j <= n - 1);
  return coeff[j];
}

double& Vector::operator () (int j) {
  assert(0 <= j && j <= n - 1);
  return coeff[j];
}
