def calculate_expression(expression: str):
    try:
        # Only allow numbers and arithmetic symbols
        allowed_chars = "0123456789+-*/(). "
        if not all(char in allowed_chars for char in expression):
            return "Error: Invalid characters detected."

        # Evaluate the expression safely
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    expr = input("Enter a mathematical expression: ")
    output = calculate_expression(expr)
    print("Result:", output)
