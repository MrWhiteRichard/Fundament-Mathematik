#include "complex.hpp"

Complex::Complex (double real, double imag) {
  re = real;
  im = imag;
}

double Complex::real () const { return re; }
double Complex::imag () const { return im; }
double Complex::abs () const { return sqrt(re*re + im*im); }

const Complex Complex::operator - () const { return Complex(-re, -im); }
const Complex Complex::operator ~ () const { return Complex(re, -im); }

const Complex operator + (const Complex& z, const Complex& w) {
  double Re_z = z.real();
  double Im_z = z.imag();
  double Re_w = w.real();
  double Im_w = w.imag();

  return Complex(Re_z + Re_w, Im_z + Im_w);
}

const Complex operator - (const Complex& z, const Complex& w) {
  return z + (-w);
}

const Complex operator * (const Complex& z, const Complex& w) {
  double Re_z = z.real();
  double Im_z = z.imag();
  double Re_w = w.real();
  double Im_w = w.imag();

  return Complex(Re_z*Re_w - Im_z*Im_w, Re_z*Im_w + Im_z*Re_w);
}

const Complex operator / (const Complex& z, const Complex& w) {
  double norm = z.abs();
  assert(norm != 0);

  return z * (~w) / w;
}

const bool operator < (const Complex& z, const Complex& w) {
  double Re_z = z.real();
  double Im_z = z.imag();
  double Re_w = w.real();
  double Im_w = w.imag();

  double norm_z = z.abs();
  double norm_w = w.abs();

  if (norm_z < norm_w) { return true; }
  if (norm_z == norm_w && Re_z < Re_w) { return true; }
  if (norm_z == norm_w && Re_z == Re_w && Im_z < Im_w) { return true; }

  return false;
}
