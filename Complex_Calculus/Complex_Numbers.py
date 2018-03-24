"""
This program defines basic Complex number class to use in other programs : Julia Set , Mandelbrot Set etc.
"""

import math

class Complex_Number():
    def __init__(self , real_part , imaginary_part):
        """
        This function initializes a complex number
        """

        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        """
        This function prints a particular Complex_Number object
        """
        s = str(self.real_part)
        if self.imaginary_part == 0:
            return s
        elif self.imaginary_part > 0:
            s += " + "
        else:
            s += " - "
        s += str(abs(self.imaginary_part)) # Use abs to avoid double -
        s += "i"
        return s

    def get_clone(self):
        """
        Returns the copy of the complex number
        """
        new_complex = Complex_Number(self.real_part , self.imaginary_part)

        return new_complex

    def get_real(self):
        """
        This function returns the real part of a complex number
        """
        return self.real_part

    def get_imaginary(self):
        """
        This function returns the imaginary part of a complex number
        """
        return self.imaginary_part

    def compute_modulus(self):
        """
        This function computes modulus of a complex number
        """
        return self.real_part * self.real_part + self.imaginary_part * self.imaginary_part

    def sum_complex_numbers(self , other_complex_number):
        """
        This function sum up two complex numbers and return the result as a complex number
        """
        sum = Complex_Number(self.real_part + other_complex_number.real_part , self.imaginary_part + other_complex_number.imaginary_part)
        return sum

    def multiply_complex_numbers(self , other_complex_number):
        """
        This function multiply two complex numbers and return the result as a complex number
        """
        result_real = self.real_part * other_complex_number.real_part - self.imaginary_part * other_complex_number.imaginary_part
        result_imaginary = self.real_part * other_complex_number.imaginary_part + self.imaginary_part * other_complex_number.real_part
        result = Complex_Number(result_real , result_imaginary)
        return result

    def compute_conjugate(self):
        """
        This function returns the conjugate of the complex number
        """
        result = Complex_Number(self.real_part , -self.imaginary_part)
        return result

    def multiply_constant(self , constant):
        """
        This function multiply a complex number with a real constant and returns the resulting complex number
        """
        result = Complex_Number(self.real_part * constant , self.imaginary_part * constant)
        return result
