"""
This is the calculator file, wherein functions will be added using branch workflows
I will implement regular and matrix calculator seperately via operations
"""

def float_add():
    """Adds two float values from user input and prints the sum."""
    val1 = float(input("Enter first value: "))
    val2 = float(input("Enter second value: "))
    result = val1 + val2
    print(f"{val1} + {val2} = {result}")
    

""" Testing """
float_add()
