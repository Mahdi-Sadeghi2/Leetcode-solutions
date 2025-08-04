# Time complexity O(n) | Space complexity O(n)


def evalRPN(tokens) -> int:
    stack = []  # Stack to store operands

    # Dictionary mapping operators to their corresponding lambda functions
    valid_operators = {
        "+": lambda n1, n2: n1 + n2,   # Addition
        "-": lambda n1, n2: n1 - n2,   # Subtraction
        "*": lambda n1, n2: n1 * n2,   # Multiplication
        # Division with truncation toward zero
        "/": lambda n1, n2: int(n1 / n2),
    }

    for token in tokens:
        if token in valid_operators:
            # When we encounter an operator:
            n2 = stack.pop()  # Pop the right operand (last in)
            n1 = stack.pop()  # Pop the left operand (second last in)

            # Get the operation function from our dictionary
            operation = valid_operators[token]

            # Perform the operation and get result
            result = operation(n1, n2)

            # Push the result back onto the stack
            stack.append(result)
        else:
            # For numbers, convert to int and push to stack
            stack.append(int(token))

    # The final result will be the only item left on the stack
    return stack.pop()
