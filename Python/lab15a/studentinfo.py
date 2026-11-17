students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82],
    },
}

print("STUDENT INFORMATION MANAGEMENT SYSTEM")

while True:
    print("\n1.View All 2.Search 3.Register 4.Update 5.Performance 6.Delete 7.Exit")
    choice = input("Enter choice (1-7): ").replace(" ", "")

    if choice == "1":
        for roll, info in students.items():
            print(
                f"Roll No: {roll} | Name: {info['Name']} | Branch: {info['Branch']} | Sem: {info['Semester']} | Marks: {info['Marks']}"
            )
        print(f"Total: {len(students)}")

    elif choice == "2":
        roll = input("Enter Roll: ").replace(" ", "")
        s = students.get(roll)
        if s:
            print(f"[FOUND] {s}")
        else:
            print("[NOT FOUND]")

    elif choice == "3":
        roll = input("Enter Roll Number: ").replace(" ", "")
        if roll in students:
            print("[ERROR] Already exists")
        else:
            name = input("Enter Student Name: ").replace(" ", "")
            branch = input("Enter Branch: ").replace(" ", "")
            sem = input("Enter Semester: ").replace(" ", "")
            m1 = int(input("Subject 1: ").replace(" ", ""))
            m2 = int(input("Subject 2: ").replace(" ", ""))
            m3 = int(input("Subject 3: ").replace(" ", ""))
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": sem,
                "Marks": [m1, m2, m3],
            }
            print(f"[SUCCESS] {name} registered")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ").replace(" ", "")
        if roll in students:
            print(
                f"Current: 1.Branch:{students[roll]['Branch']} 2.Semester:{students[roll]['Semester']}"
            )
            opt = input("Choose 1 for Branch, 2 for Semester: ").replace(" ", "")
            if opt == "1":
                students[roll]["Branch"] = input("Enter new branch: ").replace(" ", "")
            else:
                students[roll]["Semester"] = input("Enter new semester: ").replace(" ", "")
            print("[SUCCESS] Updated")
        else:
            print("[NOT FOUND]")

    elif choice == "5":
        roll = input("Enter Roll for Academic Performance: ").replace(" ", "")
        s = students.get(roll)
        if s:
            total = sum(s["Marks"])
            avg = total / 3
            result = "PASS" if avg >= 40 else "FAIL"
            print(
                f"Name: {s['Name']} Roll:{roll} Total:{total}/300 Avg:{avg:.2f}% Result:{result}"
            )

    elif choice == "6":
        roll = input("Enter Roll to delete: ").replace(" ", "")
        if students.pop(roll, None):
            print("[SUCCESS] Deleted")
        else:
            print("[NOT FOUND]")

    elif choice == "7":
        break