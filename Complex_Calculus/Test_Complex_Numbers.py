"""
This program tests Complex_Numbers.py
"""

import Complex_Numbers as cmp

def test():
    """
    Manual testing for Complex_Number class
    """
    first_complex_num = cmp.Complex_Number(5 , 4)
    print("First complex number is :" , str(first_complex_num))
    second_complex_num = cmp.Complex_Number(3, -2)
    print("Second complex number is:" , str(second_complex_num))
    third_complex_num = cmp.Complex_Number(1 , 0)
    print("Third complex number is:" , str(third_complex_num))
    sum1 = first_complex_num.sum_complex_numbers(second_complex_num)
    print("Sum of" , str(first_complex_num) , "and" , str(second_complex_num) , "is :" , str(sum1))
    mult1 = second_complex_num.multiply_complex_numbers(third_complex_num)
    print("Multiplying" , str(second_complex_num) , "with" , str(third_complex_num) , "yields" , str(mult1))
    modulus1 = first_complex_num.compute_modulus()
    print("Modulus of" , str(first_complex_num) , "is" , modulus1)
    conj2 = second_complex_num.compute_conjugate()
    print("Conjugate of" , str(second_complex_num) , "is" , conj2)

#To run the test uncomment the following line..
test()
