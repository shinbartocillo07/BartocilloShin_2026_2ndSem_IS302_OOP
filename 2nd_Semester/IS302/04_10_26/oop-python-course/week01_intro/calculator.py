num1_SGB = float(input("Enter first number: "))
num2_SGB = float(input("Enter second number: "))

print("Addition:", num1_SGB + num2_SGB)
print("Subtraction:", num1_SGB - num2_SGB)
print("Multiplication:", num1_SGB * num2_SGB)

if num2_SGB != 0:
    print("Division:", num1_SGB / num2_SGB)
else:
    print("Division: Cannot divide by zero")
