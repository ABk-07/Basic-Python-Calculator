# Define a calculator function that takes two numbers as input
def calculator(num1, num2):
    # Ask the user to enter an operator
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform addition if the operator is "+"
    if operator == "+":
        return num1 + num2
    # Perform subtraction if the operator is "-"
    elif operator == "-":
        return num1 - num2
    # Perform multiplication if the operator is "*"
    elif operator == "*":
        return num1 * num2
    # Perform division if the operator is "/"
    elif operator == "/":
        # Check if the second number is zero to avoid division error
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        # Handle invalid operator input
        return "Error: Invalid operator entered."

try:
    # Ask the user to enter the first number
    num1 = float(input("Enter the first number: "))
    # Ask the user to enter the second number
    num2 = float(input("Enter the second number: "))

    # Call the calculator function with the two numbers
    result = calculator(num1, num2)
    # Display the result of the calculation
    print("The result is:", result)

# Handle invalid number input (e.g., if the user enters letters instead of numbers)
except ValueError:
    print("Error: Please enter valid numbers.")
