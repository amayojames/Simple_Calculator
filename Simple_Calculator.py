# My calculator program
# James Amayo

# Get input from the user
Num_1 = float(input("Enter the first number: "))
Num_2 = float(input("Enter the second number: "))
Operation = input("Enter an operation (+, -, *, /): ")

# Perform the selected operation
if Operation == "+":
    result = Num_1 + Num_2
    print(f"{Num_1} + {Num_2} = {result}")
elif Operation == "-":
    result = Num_1 - Num_2
    print(f"{Num_1} - {Num_2} = {result}")
elif Operation == "*":
    result = Num_1 * Num_2
    print(f"{Num_1} * {Num_2} = {result}")
elif Operation == "/":
    if Num_2 != 0:
        result = Num_1 / Num_2
        print(f"{Num_1} / {Num_2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please use +, -, *, or /.")