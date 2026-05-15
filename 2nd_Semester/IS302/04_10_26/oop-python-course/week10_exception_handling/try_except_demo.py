try:
    number_SGB = int(input("Enter a number: "))
    result = 100 / number_SGB
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
