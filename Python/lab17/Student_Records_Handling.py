students = {
    "101": {"Name": "Aman", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Marks": [74, 80, 82]}
}

def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print("Roll No:", roll, "| Name:", student["Name"],
          "| Marks:", student["Marks"], "| Total:", total,
          "| Average:", format(average, ".2f"))

def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("[ERROR] This Roll Number already exists.")
        return

    name = input("Enter Student Name: ")
    marks = []
    for i in range(3):
        marks.append(int(input("Enter marks for subject " + str(i + 1) + ": ")))

    students[roll] = {"Name": name, "Marks": marks}
    print("[SUCCESS] Student record added successfully.")

while True:
    print("\nSTUDENT RECORDS MANAGEMENT SYSTEM")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        if students:
            for roll, student in students.items():
                display_student(roll, student)
            print("Total Students:", len(students))
        else:
            print("No student records available.")

    elif choice == "2":
        add_student()

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        if student:
            print("[RECORD FOUND]")
            display_student(roll, student)
        else:
            print("[ERROR] No student found with Roll Number", roll)

    elif choice == "4":
        print("Thank you for using the Student Records System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
