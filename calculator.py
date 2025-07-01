#This is a simple calculator for beginners
#Step 1: Ask the user to enter two numbers 
num1 =float(input("Enter the first number: "))
num2 =float(input("Enter the second number: "))
#Step 2: Ask the user to choose an operation
print("Choose an operation :")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation =input("Enter your choice (+,-, *, /): ")
# Step 3: Perform the operation using if-else
if operation == '+':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError: Cannot divide by zero.")

else:
    print("\nInvalid operation. Please enter +, -, * or /.")
    
