"""

This is the calculator file, wherein functions will be added using branch workflows
I will implement regular and matrix calculator in a more streamlined fashion
through the use of if statements

"""

import numpy as np

def calculator():
    choice = int(input("Please indicate which two-operand calculator to use. 1 = Regular values, 2 = 2x2 Matrix Calculator: "))
    if(choice == 1):
        float_calc()
    elif(choice == 2):
        matrix_calc()
    else:
        print("You have provided an invalid input.")
        calculator()

def float_calc():
    print("This is a two-operand calculator!")
    
    val1 = float(input("Please input the first operand: "))
    op = input("Please indicate your desired operation (+, -, /, *): ")
    val2 = float(input("Please input the second operand: "))
    
    """if-statement to apply operation to operand"""
    if(op == "+"):
        result = val1 + val2
    elif(op == "-"):
        result = val1 - val2
    elif(op == "*"):
        result = val1 * val2
    elif(op == "/"):
        result = val1 / val2
    else:
        print("Invalid operation provided...")
        float_calc()
    """ Result displayed """
    print(f"{val1} {op} {val2} = {result}")
    recursion()

def matrix_calc():
    print("2x2 matrix addition!")
    val1 = input("Enter four values for first matrix, each seperated by a single space: ").split()
    mat1 = np.array([ [float(val1[0]), float(val1[1])], [float(val1[2]) , float(val1[3])] ])
    op = input("Please indicate your desired operation (+, -, /, *): ")
    val2 = input("Enter four values for second matrix, each seperated by a single space: ").split()
    mat2 = np.array([ [float(val2[0]), float(val2[1])], [float(val2[2]) , float(val2[3])] ])
    result = np.add(mat1, mat2)

    """if-statement to apply operation to operand"""
    if(op == "+"):
        result = np.add(mat1, mat2)
    elif(op == "-"):
        result = np.subtract(mat1, mat2)
    elif(op == "*"):
        result = np.multiply(mat1, mat2)
    elif(op == "/"):
        result = np.divide(mat1, mat2)
    else:
        print("Invalid operation provided...")
        matrix_calc()
        """Result displayed"""
    print(f"The matrix addition of {mat1} and {mat2} is {result}")
    recursion()

def recursion():
    ask = str(input("Would you like to use the calculator again? (Y/N): "))
    if(ask == "Y" or ask == "y"):
        calculator()
    elif(ask == "N" or ask == "n"):
        print("Thank you for using my calculator!")
    else:
        print("Invalid input, try again!")
        recursion()


""" Code is called upon """
calculator()