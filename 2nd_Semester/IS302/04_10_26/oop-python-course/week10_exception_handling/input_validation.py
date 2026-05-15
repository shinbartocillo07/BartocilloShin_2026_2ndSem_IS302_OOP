while True:
    try:
        number_SGB = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Valid number entered:", number_SGB)
