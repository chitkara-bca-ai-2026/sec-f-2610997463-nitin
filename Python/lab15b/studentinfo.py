students = {
    101: {"Name": "Aman", "Branch": "BCA AI", "Semester": 1, "Marks": [85, 90, 78]},
    102: {"Name": "Riya", "Branch": "BCA AI", "Semester": 1, "Marks": [92, 88, 95]},
    103: {
        "Name": "Karan",
        "Branch": "BCA General",
        "Semester": 1,
        "Marks": [45, 38, 50],
    },
}

print("Student Info Management System")

while True:
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ").replace(" ", "")

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice! Please enter between 1 to 7.")
        continue

    if choice == "1":
        if len(students) == 0:
            print("No records found.")
        else:
            print("\n--- Enrolled Student Records ---")
            for roll, data in students.items():
                print(
                    f"Roll No: {roll} | Name: {data['Name']} | Branch: {data['Branch']} | Sem: {data['Semester']} | Marks: {data['Marks']}"
                )
            print(f"Total Students: {len(students)}")

    elif choice == "2":
        roll = int(input("Enter Roll Number to search: ").replace(" ", ""))
        data = students.get(roll)
        if data:
            print(f"\nDetails for Roll No {roll}:")
            print(f"Name: {data['Name']}")
            print(f"Branch: {data['Branch']}")
            print(f"Semester: {data['Semester']}")
            print(f"Marks: {data['Marks']}")
        else:
            print(f"Student with Roll No {roll} not found.")

    elif choice == "3":
        roll = int(input("Enter Roll Number: ").replace(" ", ""))
        if roll in students:
            print(f"Roll No {roll} already exists!")
        else:
            name = input("Enter Name: ").replace(" ", "")
            branch = input("Enter Branch: ").replace(" ", "")
            sem = int(input("Enter Semester: ").replace(" ", ""))
            m1 = int(input("Enter Mark 1: ").replace(" ", ""))
            m2 = int(input("Enter Mark 2: ").replace(" ", ""))
            m3 = int(input("Enter Mark 3: ").replace(" ", ""))
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": sem,
                "Marks": [m1, m2, m3],
            }
            print(
                f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully."
            )

    elif choice == "4":
        roll = int(input("Enter Roll Number to update: ").replace(" ", ""))
        if roll in students:
            print(f"Current details for {students[roll]['Name']} (Roll {roll}):")
            print(
                f"1. Branch: {students[roll]['Branch']} | 2. Semester: {students[roll]['Semester']}"
            )
            opt = input("Choose field to update (1 for Branch, 2 for Semester): ").replace(" ", "")
            if opt == "1":
                new_branch = input("Enter new Branch: ").replace(" ", "")
                students[roll]["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif opt == "2":
                new_sem = int(input("Enter new semester: ").replace(" ", ""))
                students[roll]["Semester"] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("Invalid option.")
        else:
            print(f"Student with Roll No {roll} not found.")

    elif choice == "5":
        roll = int(input("Enter Roll Number for Academic Performance: ").replace(" ", ""))
        data = students.get(roll)
        if data:
            total = sum(data["Marks"])
            avg = total / len(data["Marks"])
            result = "PASS" if avg >= 40 else "FAIL"
            print(f"\n================ ACADEMIC REPORT ================")
            print(f"Student Name : {data['Name']} (Roll: {roll})")
            print(f"Subject Marks: {data['Marks']}")
            print(f"Total Marks  : {total} / 300")
            print(f"Average Marks: {avg:.2f}%")
            print(f"Final Result : {result}")
            print(f"===============================================")
        else:
            print(f"Student with Roll No {roll} not found.")

    elif choice == "6":
        roll = int(input("Enter Roll Number to delete: ").replace(" ", ""))
        deleted = students.pop(roll, None)
        if deleted:
            print(
                f"\n[SUCCESS] Record for '{deleted['Name']}' (Roll No: {roll}) deleted successfully."
            )
        else:
            print(f"Student with Roll No {roll} not found.")

    elif choice == "7":
        print("Thank you for using Student Info Management System. Goodbye!")
        break