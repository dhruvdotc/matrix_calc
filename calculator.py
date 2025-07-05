"""

This is the calculator file, wherein functions will be added using branch workflows
I will implement regular and matrix calculator in a more streamlined fashion
through the use of if statements

"""

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

print(f"{val1} {op} {val2} = {result}")
