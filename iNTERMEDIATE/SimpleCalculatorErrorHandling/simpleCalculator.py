import re


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def calculate(expresion):
    try:
        # Use regular expresions to validate and parse the input
        pattern = r'^\s*(-?\d+(\.\d+)?)\s*([+\-*/])\s*(-?\d+(\.\d+)?)\s*$'
        match = re.match(pattern, expresion)
        print(f"Match: {match}")
        print(f"Match gr1: {match.group(1)}")
        print(f"Match gr2: {match.group(2)}")
        print(f"Match gr3: {match.group(3)}")
        print(f"Match gr4: {match.group(4)}")
        if not match:
            raise ValueError("Invalid input. Please enter a valid expression.")

        operand1, operator, operand2 = float(match.group(1)), match.group(3), float(match.group(4))

        # Perform the appropriate operation
        if operator == '+':
            result = add(operand1, operand2)
        elif operator == '-':
            result = substract(operand1, operand2)
        elif operator == '*':
            result = multiply(operand1, operand2)
        elif operator == '/':
            result = divide(operand1, operand2)
        else:
            raise ValueError("Unknown operator.")

        return result
    except ValueError as ve:
        return f"Error: {ve}"


def main():
    print("Simpler Calculator. Enter expressions in the format: operand1 operator operand2")
    print("Type 'exit' to quit.")
    while True:
        expression = input("Enter expression: ").strip()
        if expression.lower() == 'exit':
            break
        result = calculate(expression)
        print(result)


if __name__ == '__main__':
    main()