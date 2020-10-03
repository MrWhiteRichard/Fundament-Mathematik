#include "vector.cpp"

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char const *argv[]) {
  int n = 3869;

  Vector x = foo(n);
  Vector y = eratosthenes(n);

  cout << endl;
  x.printVector();

  cout << n << " = ";
  for (size_t i = 0; i < x.size(); i++) {
    if ( x(i) != 0) {
      cout << y(i) << "^" << x(i) << " * ";
    }
  }
  cout << 1 << endl;
  return 0;
}
