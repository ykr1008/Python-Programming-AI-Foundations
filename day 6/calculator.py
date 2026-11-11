
class DivisionByZeroError(Exception):
    """Raised when attempting to divide by zero."""
    pass


def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {op}")


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        result = calculate(a, b, op)

    except DivisionByZeroError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")

    else:
        print(f"Result: {result}")

    finally:
        print("Calculation attempted.")


if __name__ == "__main__":
    main()
