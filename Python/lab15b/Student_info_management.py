students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]}
}

print("="*55)
print("STUDENT INFORMATION MANAGEMENT SYSTEM")
print("="*55)

while True:
    print()
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    print()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print()
        print("--- Enrolled Student Records ---")
        for roll, info in students.items():
            print(f"Roll No: {roll} | Name: {info['Name']} | Branch: {info['Branch']} | Sem: {info['Semester']} | Marks: {info['Marks']}")
        print(f"Total Enrolled Students: {len(students)}")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        data = students.get(roll)
        print()
        if data:
            print(f"[FOUND] Record for Roll No {roll}:")
            print(f"  Name     : {data['Name']}")
            print(f"  Branch   : {data['Branch']}")
            print(f"  Semester : {data['Semester']}")
            print(f"  Marks    : {data['Marks']}")
        else:
            print(f"[NOT FOUND] Roll No {roll} does not exist.")

    elif choice == "3":
        print()
        print("--- Register New Student ---")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print(f"[ERROR] Roll No {roll} already exists!")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            sem = input("Enter Semester: ")
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("  Subject 1: "))
            m2 = int(input("  Subject 2: "))
            m3 = int(input("  Subject 3: "))
            students[roll] = {"Name": name, "Branch": branch, "Semester": sem, "Marks": [m1, m2, m3]}
            print()
            print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        data = students.get(roll)
        if data:
            print(f"Current details for {data['Name']} (Roll {roll}):")
            print(f"1. Branch: {data['Branch']} | 2. Semester: {data['Semester']}")
            opt = input("Choose field to update (1 for Branch, 2 for Semester): ")
            if opt == "1":
                new_branch = input("Enter new branch: ")
                students[roll]["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif opt == "2":
                new_sem = input("Enter new semester: ")
                students[roll]["Semester"] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("[ERROR] Invalid choice")
        else:
            print(f"[NOT FOUND] Roll No {roll}")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")
        student = students.get(roll)
        if student:
            marks = student["Marks"]
            total = sum(marks)
            avg = total / len(marks)
            result = "PASS" if avg >= 40 else "FAIL"
            print()
            print("============== ACADEMIC REPORT ==============")
            print(f"Student Name: {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {marks}")
            print(f"Total Marks : {total} / 300")
            print(f"Average Marks: {avg:.2f}%")
            print(f"Final Result : {result}")
            print("==============================================")
        else:
            print(f"[NOT FOUND] Roll No {roll}")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")
        removed = students.pop(roll, None)
        print()
        if removed:
            print(f"[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"[NOT FOUND] Roll No {roll}")

    elif choice == "7":
        print("Thank you for using Student Info System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Enter 1 to 7.")