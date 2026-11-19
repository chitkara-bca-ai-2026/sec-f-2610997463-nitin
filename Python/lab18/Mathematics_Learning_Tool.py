def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    print("\nMATHEMATICS LEARNING TOOL")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Please enter a non-negative number.")
        else:
            print("[RESULT] Factorial of", number, "is:", factorial(number))

    elif choice == "2":
        terms = int(input("Enter number of terms to generate: "))
        if terms < 0:
            print("Please enter zero or a positive number.")
        else:
            series = []
            for i in range(terms):
                series.append(fibonacci(i))
            print("[RESULT] Fibonacci series:", series)

    elif choice == "3":
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
