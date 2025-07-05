"""
This is a file where I was experimenting ways to make the calculator.
I prototyped creation of seperate functions for each operation but realized an 
interactive if statement would make things much more user-friendly and streamlined.

"""
import numpy as np

def float_add():
    """Adds two float values from user input and prints the sum."""
    val1 = float(input("Enter first value: "))
    val2 = float(input("Enter second value: "))
    result = val1 + val2
    print(f"{val1} + {val2} = {result}")
    

""" Testing """
float_add()

def matrix_add():
    print("2x2 matrix addition!")
    val1 = input("Enter four values for first matrix, each seperated by a single space: ").split()
    mat1 = np.array([ [float(val1[0]), float(val1[1])], [float(val1[2]) , float(val1[3])] ])
    val2 = input("Enter four values for second matrix, each seperated by a single space: ").split()
    mat2 = np.array([ [float(val2[0]), float(val2[1])], [float(val2[2]) , float(val2[3])] ])
    result = np.add(mat1, mat2)
    print(f"The matrix addition of {mat1} and {mat2} is {result}")


