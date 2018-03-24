"""
This program is implementing Julia Set class which can plot the Julia sets of a given equation using matplotlib library of python
For more information check documentation
"""

import matplotlib.pyplot as plt
import math

class Julia_Set:
    def __init__(self , constant_real = 0 , constant_imaginary = 0 , max_iter = 100 , x_lower = -1.5 , x_upper = 1.5 , y_lower = -1.5 , y_upper  =  1.5 , interval = 0.05):
        """
        This function initializes Julia_Set object
        """
        self.constant_real = constant_real
        self.constant_imaginary = constant_imaginary
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
        s += str(self.constant_real)
        s += str(" + ")
        s += str(self.constant_imaginary)
        s += "i)"
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


    def plot_Julia_Set(self):
        """
        This function plots the Julia set a particular class instance,self
        """
        r = self.compute_R()
        x_axis = []
        y_axis = []
        x_initial = self.x_lower

        while x_initial < self.x_upper :
            y_initial = self.y_lower
            while y_initial < self.y_upper :
                pre_result_real = x_initial
                pre_result_imaginary = y_initial
                for dummy_i in range(self.max_iter) :
                    result = self.compute_one_more_iter(pre_result_real , pre_result_imaginary)
                    x_result = result[0]
                    y_result = result[1]
                    modulus = compute_modulus(x_result , y_result)
                    if modulus > (r * r) :
                        break
                    if dummy_i == self.max_iter - 1:
                        x_axis.append(x_initial)
                        y_axis.append(y_initial)
                    pre_result_real = result[0]
                    pre_result_imaginary = result[1]
                y_initial += self.interval
            x_initial += self.interval
        plt.plot(x_axis , y_axis , 'ko')
        plt.axis([self.x_lower , self.x_upper , self.y_lower , self.y_upper])
        plt.show()

    def set_constant(self,constant):
        """
        This function determines the c in the formula f(z) = z^2 + c
        """
        self.constant = constant
    def get_constant(self):
        """
        This function returns the value of constant
        """
        return self.constant
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
    def compute_one_more_iter(self , real_part , imaginary_part ):
        """
        This function computes f(real_part + i * imaginary_part)
        """
        real = real_part * real_part - imaginary_part * imaginary_part + self.constant_real
        imaginary = 2 * real_part * imaginary_part + self.constant_imaginary
        return [real , imaginary]

    def compute_R(self):
        """
        This function computes R using theorem in the documentation
        """
        r = 1 + math.sqrt(1 + 4 * compute_modulus(self.constant_real , self.constant_imaginary))
        r = r / 2
        return r

def compute_modulus(real_part , imaginary_part):
    """
    This function computes the modulus of the a complex number
    """
    result = real_part * real_part + imaginary_part * imaginary_part
    return result

def run():
    julia_set = Julia_Set(constant_real = 1 , constant_imaginary = 0 , max_iter = 100 , interval = 0.05 )
    print (str(julia_set))
    julia_set.plot_Julia_Set()

run()
