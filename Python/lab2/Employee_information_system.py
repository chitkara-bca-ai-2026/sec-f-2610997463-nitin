#  Employee Information System   

# ask details and print data type with it
emp_name = input("Enter Employee Name: ") 
print(f"Data type: {type(emp_name)}") # type(), to check the data type

emp_id = int(input("Enter Employee ID: ")) 
print(f"Data type: {type(emp_id)}")

salary = float(input("Enter Salary: ")) 
print(f"Data type: {type(salary)}")

department = input("Enter Department: ") # for department string
print(f"Data type: {type(department)}")

active_input = input("Is the employee active? (yes/no): ")
is_active = True if active_input.lower() == 'yes' else False  # lower() that to find any lowercase
print(f"Data type: {type(is_active)}")

# print all details together
print("\n--- Employee Details ---")
print(f"Name       : {emp_name}")
print(f"ID         : {emp_id}")
print(f"Salary     : {salary}")
print(f"Department : {department}")
print(f"Active     : {is_active}")