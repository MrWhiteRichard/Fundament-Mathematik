#include "trimatrix.hpp"

TriMatrix::TriMatrix (int n, double init) {
  assert(0 <= n);

  this->n = n;
  int length = n*(n + 1)/2;

  if (n == 0) { coeff = (double*) 0; }
  else { coeff = new double[length]; }

  for (int i = 0; i < length; i++) { coeff[i] = init; }
}

//TriMatrix (const TriMatrix&);

TriMatrix::~TriMatrix () { delete[] coeff; }

TriMatrix& TriMatrix::operator = (const TriMatrix& rhs) {
  if (this != &rhs) {
    n = rhs.size();
    int length = n*(n + 1)/2;

    delete coeff;
    coeff = new double[length];

    for (int i = 0; i < n; i++) {
      for (int j = i; j < n; j++) {
        coeff[j*(j + 1)/2 + i] = rhs(j, i);
      }
    }
  }

  return *this;
}

int TriMatrix::size () const { return n; }

const double& TriMatrix::operator () (int j, int k) const {
  assert(0 <= k && k <= j && j <= n - 1);
  return coeff[j*(j + 1)/2 + k];
}

//double& operator () (int j, int k);

double max (double x[], int dim) {
  assert(dim > 0);
  double max = x[0];

  for (int i = 1; i < dim; i++) {
    if (max < x[i]) {
      max = x[i];
    }
  }

  return max;
}

double TriMatrix::norm () const {
  double x[n];

  for (int i = 0; i < n; i++) {
    x[i] = 0;

    for (int j = 0; j <= i; j++) { x[i] += fabs(coeff[i*(i + 1)/2 + j]); }

    return max(x, n);
  }
}

const TriMatrix operator * (TriMatrix& A, TriMatrix& B) {
  assert(A.size() == B.size() );

  double tmp;
  TriMatrix AB( A.size() );

  for (int i = 0; i < A.size(); i++) { // in welcher Spalte bin ich
    for (int j = i; j < A.size(); j++) { // in welcher Zeile bin ich
      tmp = 0;
      for (int a = i; a <= j; a++) { tmp += A(j, a)*B(a, i); }
      AB.setMatrix(j, i, tmp);
    }
  }

  return AB;
}
