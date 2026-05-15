try:
    num1_SGB = float(input("Enter first number: "))
    num2_SGB = float(input("Enter second number: "))
    result = num1_SGB / num2_SGB
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid numeric input")
