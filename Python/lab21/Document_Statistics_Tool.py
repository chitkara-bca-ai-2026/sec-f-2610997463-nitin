import os

def get_document_statistics(filename):
    with open(filename, "r") as file:
        content = file.read()

    line_count = len(content.splitlines())
    word_count = len(content.split())
    char_count = len(content)

    return line_count, word_count, char_count

def display_document(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    print("\n--- Document Preview ({}) ---".format(filename))
    for number, line in enumerate(lines, start=1):
        print(number, "|", line.rstrip())

filename = "document.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("Artificial Intelligence is transforming modern industries.\n")
        file.write("Python provides powerful libraries for text processing and data analysis.\n")
        file.write("Developers use file handling to store and retrieve persistent records.\n")
        file.write("Modular programming ensures code is clean, reusable, and easy to maintain.\n")

while True:
    print("\nDOCUMENT STATISTICS ANALYZER")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        lines, words, characters = get_document_statistics(filename)
        print("\n----------- DOCUMENT REPORT -----------")
        print("Target File   :", filename)
        print("Total Lines   :", lines)
        print("Total Words   :", words)
        print("Total Characters:", characters)
        print("---------------------------------------")

    elif choice == "2":
        display_document(filename)

    elif choice == "3":
        print("Thank you for using Document Statistics Analyzer. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
