# Importing the 'logo' from art module for the calculator interface.
from art import logo

# Defining basic arithmetic functions.
def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def sub(n1, n2):
    """Returns the difference between two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Returns the quotient of two numbers, handling division by zero."""
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2

def mod(n1, n2):
    """Returns the remainder of the division of two numbers."""
    if n2 == 0:
        return "Cannot perform modulo with zero"
    return n1 % n2

# Dictionary to map operations symbols to the corresponding functions.
operation_dic = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
    "%": mod,
}

def calculator():
    """Runs a basic calculator allowing sequential operations on results."""
    print(logo)
    print("CALCULATOR IS WAITING FOR YOUR NUMBERS TO EXECUTE :)\n")
    continue_calc = True

    # First number input
    n1 = float(input("Enter the first number: "))

    while continue_calc:
        # Second number input
        n2 = float(input("Enter the next number: "))

        # Display available operations to the user
        print("Select an operation from the following:")
        for symbol in operation_dic:
            print(symbol)

        # Operation selection and validation
        operation = input("Enter your choice of operation: ")
        if operation in operation_dic:
            result = operation_dic[operation](n1, n2)
            print(f"\t{n1} {operation} {n2} = {result}")
        else:
            print("Invalid operation selected. Please try again.")
            continue

        # Prompt user to continue or restart
        next_step = input(f"Continue with result ({result})? Type 'Y' for Yes, 'N' to start new calculation: ").lower()
        if next_step == 'n':
            # Restart calculator if user chooses to start fresh
            calculator()
            break
        else:
            # Update n1 with result to continue calculation
            n1 = result


calculator()