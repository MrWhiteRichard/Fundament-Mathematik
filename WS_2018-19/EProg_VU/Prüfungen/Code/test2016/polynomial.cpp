#include "polynomial.hpp"

Polynomial::Polynomial (int n) {
  assert(n >= 0);

  this->n = n;
  a = new double[n + 1];

  for (int i = 0; i < n + 1; i++) { a[i] = 0; }
}

Polynomial::Polynomial (const Polynomial& p) {
  n = p.degree();

  if (n == 0) { a = (double*) 0; }
  else { a = new double[n + 1]; }

  for (int i = 0; i < n + 1; i++) { a[i] = p[i]; }
}

Polynomial::~Polynomial () { delete[] a; }

Polynomial& Polynomial::operator = (const Polynomial & rhs) {
  if (this != &rhs) {
    n = rhs.degree();
    delete[] a;
    a = new double[n + 1];

    for (int i = 0; i < n + 1; i++) { a[i] = rhs[i]; }
  }

  return *this;
}

int Polynomial::degree () const { return n; }

Polynomial Polynomial::diff () const {
  if (n == 0) {
    Polynomial p;
    return p;
  }
  else {
    Polynomial p(n - 1);
    for (int i = 0; i < n; i++) { p.a[i] = (i + 1)*a[i + 1]; }
    return p;
  }
}

double Polynomial::operator () (double x) const {
  double output = 0;
  double potenz = 1;

  for (int i = 0; i <= n; i++) {
    output += a[i]*potenz;
    potenz *= x;
  }

  return output;
}

const double& Polynomial::operator [] (int j) const {
  assert(0 <= j && j <= n);
  return a[j];
}

double& Polynomial::operator [] (int j) {
  assert(0 <= j && j <= n);
  return a[j];
}

int max (int n, int m) {
  if (n < m) { return m; }
  else { return n; }
}

const Polynomial operator + (const Polynomial& p, const Polynomial& q) {
  int n = max(p.degree(), q.degree() );
  Polynomial bobo(n);

  for (int i = 0; i <= p.degree(); i++) { bobo.a[i] += p[i]; }
  for (int i = 0; i <= q.degree(); i++) { bobo.a[i] += q[i]; }

  return bobo;
}

const Polynomial operator * (const double& x, const Polynomial& p) {
  Polynomial fritz(p.degree() );

  for (int i = 0; i <= p.degree(); i++) { fritz.a[i] += x*p[i]; }

  return fritz;
}

const Polynomial operator * (const Polynomial& p, const double& x) {
  Polynomial fritz(p.degree() );

  for (int i = 0; i <= p.degree(); i++) { fritz.a[i] += p[i]*x; }

  return fritz;
}

const Polynomial operator * (const Polynomial& p, const Polynomial& q) {
  Polynomial karl(p.degree() + q.degree() );

  for (int i = 0; i <= p.degree(); i++) {
    for (int j = 0; j <= q.degree(); j++) {
      karl.a[i + j] += p[i]*q[j];
    }
  }

  return karl;
}

double root (const Polynomial p, double x_0 = 0, double tol = 1e-15) {
  assert(tol > 0);
  Polynomial q = p.diff();
  double x_k_down;
  double x_k = x_0;

  do {
    x_k_down = x_k;
    x_k = x_k_down + p(x_k_down)/q(x_k_down);
  } while( !( fabs( p(x_k) ) <= tol && fabs(x_k - x_k_down) <= tol ) );

  return x_k;
}
