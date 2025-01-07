import math
print("Welcome to the Basic Calculator Program in Python!\n")

# Defining functions for basic operations
def sum(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Raises an error if dividing by zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero. Please provide a non-zero divisor.")
    return a / b

def square(a):
    """Returns the square of the first entered number"""
    return a*a

def square_root(a):
    """Returns the square root of the first entered number"""
    if a<=-1:
        print("Complex Calculations are not permitted")
    return pow(a,0.5)

def power(base, exponent):
    """Returns the exponentiation of the first number entered by the user to the second number as power"""
    return base**exponent

def modulus(a, b): 
    return a % b

def logarithm(a): 
    if a <= 0: 
        raise ValueError("Logarithm undefined for non-positive numbers.") 
    return math.log(a)
    

# Loop to allow repeated calculations
while True:
    print("Now, enter two numbers (integer only) for calculation along with the operator\n")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter integers or floats only.")
        continue

    print("""Choose from the below listed operations: 
    1. For Addition = +
    2. For Subtraction = -
    3. For Multiplication = *
    4. For Division = /
    5. For Squaring of first number = square 
    6. For Square root of the first number = square_root
    7. For finding the first number raised to the pwoer secodn number = power
    8. For Finding the Remainder while dividing those numbers = Remainder
    9. For Finding the log of the first number to the base second number = log 
    """)

    # Entering the operation symbol for execution
    op = input("Enter the operation symbol that needs to be performed: ")

    match op:
        case "+":
            print("The addition of numbers is: ", sum(num1, num2))
        case "-":
            print("The subtraction of numbers is: ", subtract(num1, num2))
        case "*":
            print("The multiplication of numbers is: ", multiply(num1, num2))
        case "/":
            try:
                print("The division of numbers is: ", divide(num1, num2))
            except ZeroDivisionError as e:
                print(e)
        case "square":
            print("The square of the first entered number is: ", square(num1))
        case "square_root":
            print("The square-root of the first entered number is: ", square_root(num1))
        case "power":
            print("The first number rasied ot the second number as power: ", power(num1,num2))
        case "Remainder":
            print("The Remaidner of those numbers is: ", modulus(num1,num2))
        case "log":
            print("Log of first number to the base e: ", logarithm(num1))
        case _:
            print("Invalid operator symbol. Please choose from ( + , - , * , / ).")

    # Prompt to perform another calculation
    repeat = input("Do you want to perform another calculation? (y/n): ")
    if repeat.lower() != 'y':
        print("Exiting the calculator. Goodbye!")
        break
