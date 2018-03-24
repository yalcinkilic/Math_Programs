"""
This program is implementing Julia Set class which can plot the Julia sets of a given equation using matplotlib library of python
For more information check documentation
"""

import matplotlib.pyplot as plt
import Complex_Numbers as cmp
import math
import time

class Julia_Set:
    def __init__(self , complex_constant = cmp.Complex_Number(0 , 0) , max_iter = 100 , x_lower = -1.5 , x_upper = 1.5 , y_lower = -1.5 , y_upper  =  1.5 , interval = 0.05):
        """
        This function initializes Julia_Set object
        """
        self.complex_constant = complex_constant
        self.max_iter = max_iter
        self.x_lower = x_lower
        self.x_upper = x_upper
        self.y_lower = y_lower
        self.y_upper = y_upper
        self.interval = interval

    def __str__(self):
        """
        This function prints Julia_Set object
        """
        s = "The function is : z^2 + ("
        s += str(self.complex_constant)
        s += '\n'
        s += "Max iteration is : "
        s += str(self.max_iter)
        s += " x_lower is : "
        s += str(self.x_lower)
        s += " x_upper is : "
        s += str(self.x_upper)
        s += " y_lower is : "
        s += str(self.y_lower)
        s += " y_upper is : "
        s += str(self.y_upper)
        s += '\n'

        return s

    def find_Julia_Set(self):
        """
        This function finds Julia Set of given function and returns x_coordinates and y_coordinates
        """
        r = self.compute_R()
        x_axis = []
        y_axis = []
        x_temp = self.x_lower

        while x_temp < self.x_upper :
            y_temp = self.y_lower
            while y_temp < self.y_upper :
                prev_complex = cmp.Complex_Number(x_temp , y_temp)
                for dummy_i in range(self.max_iter):
                    now_complex = self.compute_one_more_iter(prev_complex)
                    modulus = now_complex.compute_modulus()
                    if modulus * modulus > r * r  :
                        break

                    if dummy_i == self.max_iter - 1 :
                        x_axis.append(x_temp)
                        y_axis.append(y_temp)

                    prev_complex = now_complex.get_clone()
                y_temp += self.interval
            x_temp += self.interval

        return x_axis , y_axis


    def plot_Julia_Set(self , x_axis , y_axis):
        """
        This function plots the Julia set a particular class instance,self
        """
        plt.plot(x_axis , y_axis , 'ko')
        plt.axis([self.x_lower , self.x_upper , self.y_lower , self.y_upper])
        plt.show()

    def set_constant(self,constant):
        """
        This function determines the c in the formula f(z) = z^2 + c
        """
        self.complex_constant = constant
    def get_constant(self):
        """
        This function returns the value of constant
        """
        return self.complex_constant
    def set_maxiter(self , max_iter):
        """
        This function sets max iteration
        """
        self.max_iter = max_iter

    def get_maxiter(self):
        """
        This function gets the value of max_iter
        """
        return self.max_iter
    def set_window(self , x_lower , x_upper , y_lower , y_upper):
        """
        This function sets the windows of the Julia set to be plotted
        """
        self.x_lower = x_lower
        self.x_upper = x_upper
        self.y_lower = y_lower
        self.y_upper = y_upper

    def get_window(self):
        """
        This function get the coordinates of the window as a list
        """
        return [self.x_lower , self.x_upper , self.y_lower , self.y_upper]
    def compute_one_more_iter(self , complex_num ):
        """
        This function computes f(real_part + i * imaginary_part)
        """
        square_complex_num = complex_num.multiply_complex_numbers(complex_num)
        return square_complex_num.sum_complex_numbers(self.complex_constant)

    def compute_R(self):
        """
        This function computes R using theorem in the documentation
        """
        r = 1 + math.sqrt(1 + 4 * self.complex_constant.compute_modulus())
        r = r / 2
        return r

def run():
    start = time.clock()
    c = cmp.Complex_Number(1/7 , 1/3)
    julia_set = Julia_Set(c, max_iter = 1000 , interval = 0.01 )
    print (str(julia_set))
    x_axis , y_axis = julia_set.find_Julia_Set()
    julia_set.plot_Julia_Set(x_axis , y_axis )
    end = time.clock()
    print("The execution time is:" , end - start , "seconds.")

run()
