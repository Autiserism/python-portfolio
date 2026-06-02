def calculator(num1, num2, operator):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2
        else:
            return "Invalid operator"
    except ZeroDivisionError:
        return "Error: cannot divide by zero"


result = calculator(10, 5, "+")
print(result)# needed notes/help
