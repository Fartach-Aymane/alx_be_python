# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """Perform basic arithmetic operations: add, subtract, multiply, divide."""
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Cannot divide by zero."
            return num1 / num2
        case _:
            return "Invalid operation. Choose add, subtract, multiply, or divide."
