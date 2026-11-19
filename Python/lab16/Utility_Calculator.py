history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Cannot find remainder with zero"
    return a % b

def power(base, exp=2):
    return base ** exp

def factor_number(value):
    if value.is_integer():
        return int(value)
    return value

while True:
    print("\nENTERPRISE MODULAR UTILITY CALCULATOR")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (Remainder)")
    print("6. Power / Exponentiation")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice in ["1", "2", "3", "4", "5"]:
        a = factor_number(float(input("Enter first number: ")))
        b = factor_number(float(input("Enter second number: ")))

        if choice == "1":
            result = add(a, b)
            symbol = "+"
        elif choice == "2":
            result = subtract(a, b)
            symbol = "-"
        elif choice == "3":
            result = multiply(a, b)
            symbol = "*"
        elif choice == "4":
            result = divide(a, b)
            symbol = "/"
        else:
            result = modulus(a, b)
            symbol = "%"

        print("[RESULT]", result)
        history.append(str(a) + " " + symbol + " " + str(b) + " = " + str(result))

    elif choice == "6":
        base = factor_number(float(input("Enter base number: ")))
        exponent = input("Enter exponent (press Enter for square): ")
        if exponent == "":
            result = power(base)
            expression = str(base) + " ** 2"
        else:
            result = power(base, factor_number(float(exponent)))
            expression = str(base) + " ** " + exponent
        print("[RESULT]", result)
        history.append(expression + " = " + str(result))

    elif choice == "7":
        if history:
            print("\n--- Calculation History ---")
            for item in history:
                print(item)
        else:
            print("No calculations have been performed yet.")

    elif choice == "8":
        print("Thank you for using the Utility Calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
