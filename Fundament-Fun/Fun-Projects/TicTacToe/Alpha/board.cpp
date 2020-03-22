// Constructor, Destructor, ...

Board::Board (int dim) {
  assert(1 <= dim && dim <= 4);
  this->dim = dim;

  int length = getVectorLength(dim);
  coeff = new int[length];
  for (size_t i = 0; i < length; i++) { coeff[i] = 0; }
}

Board::Board (const Board& input) {
  dim = input.getDim();

  int length = getVectorLength(dim);
  coeff = new int[length];
  for (size_t i = 0; i < length; i++) { coeff[i] = input[i]; }
}

Board& Board::operator = (const Board& input) {
  if (this != &input) {
    dim = input.getDim();

    int length = getVectorLength(dim);
    coeff = new int[length];
    for (size_t i = 0; i < length; i++) { coeff[i] = input[i]; }
  }

  return *this;
}

Board::~Board () { delete[] coeff; }

// get, set, ...

const int& Board::getDim () const { return dim; }

const int Board::getVectorLength (int dim) const {
  int length = 1;
  for (size_t i = 0; i < dim; i++) { length *= 3; }
  return length;
}

int& Board::operator [] (int i) {
  assert(0 <= i && i < getVectorLength(dim) );
  return coeff[i];
}

const int& Board::operator [] (int i) const {
  assert(0 <= i && i < getVectorLength(dim) );
  return coeff[i];
}

int& Board::operator () (int a, int b, int c, int d) {
  assert(0 <= a && a < 3);
  assert(0 <= b && b < 3);
  assert(0 <= c && c < 3);
  assert(0 <= d && d < 3);

  int want   = a + 3*b + 9*c + 27*d;
  int length = getVectorLength(dim);
  assert(0 <= want && want < length);

  return coeff[want];
}

const int& Board::operator () (int a, int b, int c, int d) const {
  assert(0 <= a && a < 3);
  assert(0 <= b && b < 3);
  assert(0 <= c && c < 3);
  assert(0 <= d && d < 3);

  int want   = a + 3*b + 9*c + 27*d;
  int length = getVectorLength(dim);
  assert(0 <= want && want < length);

  return coeff[want];
}

// MISC ...

ostream& operator << (ostream& output, const Board& print) {
  int until[4] = {3, 3, 3, 3};
  if (print.getDim() < 1) { until[1] = 1; }
  if (print.getDim() < 2) { until[3] = 1; }
  if (print.getDim() < 3) { until[0] = 1; }
  if (print.getDim() < 4) { until[2] = 1; }

  for (size_t k = 0; k < until[0]; k++) {
    for (size_t i = 0; i < until[1]; i++) {
      output << "  ";
      for (size_t l = 0; l < until[2]; l++) {
        for (size_t j = 0; j < until[3]; j++) {
          output << XO( print(i, j, k, l) );
          output << " ";
        }
        output << "  ";
      }
      output << endl;
    }
    output << endl;
  }

  return output;
}
