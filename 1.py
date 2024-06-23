'''
    There are 2 questions for this assignment
    Basic Calculator
    Task: Create a simple calculator that performs all arithmetic operations.
    Steps:
    - Use functions to perform each arithmetic operation.
    - Use a while loop to continuously prompt the user for actions (choose operation, input numbers, display result, exit).
    - Use arithmetic operators to perform calculations.
    - Use conditional statements to handle different user inputs and errors.

    Example interaction:
    1. Choose operation (addition)
    2. Input numbers (3, 5)
    3. Display result
    4. Exit
    Expected output: Result of the arithmetic operation.
'''
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print('This is a calculator')
print('Arithmetic Operations')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Exit')

choice = 0
while choice != 5:
    choice = int(input("Enter choice from 1 - 5 : "))

    if choice in [1, 2, 3, 4]:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
            
        if choice == 1:
            print(f"The result is: {add(num1, num2)}")
        elif choice == 2:
            print(f"The result is: {sub(num1, num2)}")
        elif choice == 3:
            print(f"The result is: {mul(num1, num2)}")
        elif choice == 4:
                print(f"The result is: {div(num1, num2)}")
    elif choice == 5:
            print("Exit.")
    else:
        print("Invalid input. Please enter a number between 1 and 5.")