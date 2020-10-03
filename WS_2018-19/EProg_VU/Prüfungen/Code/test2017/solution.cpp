#include "trimatrix.cpp"
#include "vector.cpp"

const Vector operator | (const TriMatrix& A, const Vector& b) {
  assert(A.size() == b.size() );
  double tmp;
  Vector x(b.size(), 0, "solution");

  for (int i = 0; i < b.size(); i++) {
    tmp = b(i);
    for (int j = 0; j < i; j++) {
      tmp -= A(i, j)*x(j);
    }
    tmp /= A(i, i);
    x.setVector(i, tmp);
  }

  return x;
}
