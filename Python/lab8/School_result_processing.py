print("========================================")
print("      SCHOOL RESULT PROCESSING")
print("========================================")

# student details

student_name = input("Enter Student Name : ") 
roll_number = input("Enter Roll Number  : ") 

# for taking 5 subjects  marks  from loop

marks = []    # empty list to store marks in it
total_subjects = 5
is_failed = False # pass for fail

print("\n--- Enter Marks for 5 Subjects (0-100) ---")
for i in range(1, total_subjects + 1):    # loop from 1 to 5
    m = int(input(f"Enter marks for Subject {i}: ")) 

    # marks must btw.  0-100 
    if m < 0 or m > 100:
        print("Error: Marks should be between 0 and 100.")
        exit() # if marks not in range than exit

    # if any subject marks  less than 40 fail
    if m < 40:
        is_failed = True

    marks.append(m)      #  add marks in list

#  total and percentage 
total_marks = sum(marks) 
percentage = (total_marks / 500) * 100   

# Grade 
if is_failed: 
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:     # if pass in all sub. than calculate 
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"
    else: # 40-49
        grade = "E"
        remarks = "Pass"

# print all

print("\n========================================")
print("         STUDENT REPORT CARD")
print("========================================")
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("----------------------------------------")
print(f"Total Marks  : {total_marks} / 500.0")
print(f"Percentage   : {percentage}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remarks      : {remarks}")
print("========================================")