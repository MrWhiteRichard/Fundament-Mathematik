#include "polynomial.cpp"

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char const *argv[]) {
  system("clear");

  int m, n;
  cout << "p_degree := ";
  cin >> m;
  cout << "q_degree := ";
  cin >> n;
  cout << endl;

  Polynomial p(m);
  Polynomial q(n);
  double tmp;

  for (int i = 0; i <= m; i++) {
    cout << "p_" << i << " := ";
    cin >> tmp;
    p.a[i] = tmp;
  }
  cout << endl;
  for (int i = 0; i <= n; i++) {
    cout << "q_" << i << " := ";
    cin >> tmp;
    q.a[i] = tmp;
  }
  cout << endl;

  cout << "p(x) = " << p[0] << "x^" << 0;
  for (int i = 1; i <= m; i++) {
    cout << " + " << p[i] << "x^" << i;
  }
  cout << endl;

  cout << "q(x) = " << q[0] << "x^" << 0;
  for (int i = 1; i <= n; i++) {
    cout << " + " << q[i] << "x^" << i;
  }
  cout << endl;

  Polynomial p_plus_q = p + q;

  cout << "(p + q)(x) = " << p_plus_q[0] << "x^" << 0;
  for (int i = 1; i <= p_plus_q.degree(); i++) {
    cout << " + " << p_plus_q[i] << "x^" << i;
  }
  cout << endl;

  Polynomial p_times_q = p * q;

  cout << "(p * q)(x) = " << p_times_q[0] << "x^" << 0;
  for (int i = 1; i <= p_times_q.degree(); i++) {
    cout << " + " << p_times_q[i] << "x^" << i;
  }
  cout << endl;

  return 0;
}
