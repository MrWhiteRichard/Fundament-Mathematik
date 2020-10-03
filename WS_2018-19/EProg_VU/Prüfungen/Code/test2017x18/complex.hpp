#ifndef _COMPLEX_
#define _COMPLEX_

#include <iostream>
#include <cassert>
#include <cmath>

class Complex {
private:
  double re;
  double im;

public:
  Complex (double real = 0 , double imag = 0);
  Complex& operator = (const Complex& input) {
    if (this != &input) {
      re = input.real();
      im = input.imag();
    }
    return *this;
  }

  double real () const;
  double imag () const;
  double abs () const;
  const Complex operator - () const;
  const Complex operator ~ () const;
};

const Complex operator + (const Complex&, const Complex&);
const Complex operator - (const Complex&, const Complex&);
const Complex operator * (const Complex&, const Complex&);
const Complex operator / (const Complex&, const Complex&);
const bool operator < (const Complex&, const Complex&);

const Complex operator * (const Complex& z, const double x) {
  double Re_z = z.real();
  double Im_z = z.imag();

  return Complex(Re_z*x, Im_z*x);
}

const Complex operator / (const Complex& z, const double x) {
  return z * (1/x);
}

std::ostream& operator << (std::ostream& output, const Complex& z) {
  double tol = 1e-15;
  double re = z.real();
  double im = z.imag();

  if (fabs(re) < tol && fabs(im) < tol) {
    return output << 0;
  }

  if (re > 0) {
    if (im > 0) {
      return output << fabs(re) << " + " << fabs(im) << "i";
    }
    if (im < 0) {
      return output << fabs(re) << " - " << fabs(im) << "i";
    }
    if (fabs(im) < tol) {
      return output << fabs(re);
    }
  }

  if (re < 0) {
    if (im > 0) {
      return output << "- " << fabs(re) << " + " << fabs(im) << "i";
    }
    if (im < 0) {
      return output << "- " << fabs(re) << " - " << fabs(im) << "i";
    }
    if (fabs(im) < tol) {
      return output << "- " << fabs(re);
    }
  }

  if (fabs(re) < tol) {
    if (im > 0) {
      return output << fabs(im) << "i";
    }
    if (im < 0) {
      return output << " - " << fabs(im) << "i";
    }
  }
}

#endif
