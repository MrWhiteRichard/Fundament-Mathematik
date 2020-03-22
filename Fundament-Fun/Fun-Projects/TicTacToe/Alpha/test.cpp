#include <iostream>

int random (int min, int max) {
  static bool first = true;
  if (first) {
    srand( time(NULL) );
    first = false;
  }
  return min + rand() % (( max + 1 ) - min);
}

int main(int argc, char const *argv[]) {
  std::cout << random(1, 100);
  return 0;
}
