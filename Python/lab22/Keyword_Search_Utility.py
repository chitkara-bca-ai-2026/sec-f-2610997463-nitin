import os

def search_keyword(filename, keyword):
    total = 0
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            count = line.lower().count(keyword.lower())
            if count > 0:
                print("Line", line_number, "(matches):", line.strip())
                total += count

    print("[FOUND] Total occurrences of", repr(keyword) + ":", total)

def display_document(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    print("\n--- Full Report Document ({}) ---".format(filename))
    for number, line in enumerate(lines, start=1):
        print(number, "|", line.strip())

filename = "report.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("Annual Technology and AI Progress Report.\n")
        file.write("The adoption of Artificial Intelligence accelerated across business units.\n")
        file.write("AI algorithms improved diagnostic accuracy in healthcare operations.\n")
        file.write("Data engineering pipelines were upgraded to support real-time data streaming.\n")
        file.write("The company plans further investments in AI research and machine learning.\n")

while True:
    print("\nKEYWORD SEARCH UTILITY")
    print("1. Search Keyword in Document")
    print("2. View Full Document")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        keyword = input("Enter keyword to search: ")
        search_keyword(filename, keyword)

    elif choice == "2":
        display_document(filename)

    elif choice == "3":
        print("Thank you for using Keyword Search Utility. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
