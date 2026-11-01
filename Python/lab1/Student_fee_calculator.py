# STUDENT FEES CALCULATOR


# enter all type of fees and fees type in float
tuition_fee = float(input("Enter Tuition Fee: ")) 
lab_fee = float(input("Enter Lab Fee: "))
library_fee = float(input("Enter Library Fee: ")) 
exam_fee = float(input("Enter Exam Fee: ")) 
discount = float(input("Enter Discount Amount: ")) 

# calculations of fees and discount
total_fee = tuition_fee + lab_fee + library_fee + exam_fee 
fee_after_discount = total_fee - discount 
annual_fee = fee_after_discount * 2 # multiply by 2 for both semester
monthly_installment = annual_fee / 12 

# print in this all fees and calculations
print(f"\nTuition Fee: {tuition_fee}")
print(f"Lab Fee: {lab_fee}")
print(f"Library Fee: {library_fee}")
print(f"Exam Fee: {exam_fee}")
print(f"Total Fee: {total_fee}")
print(f"Discount: {discount}")
print(f"Fee after Discount: {fee_after_discount}")
print(f"Annual Fee: {annual_fee}")
print(f"Monthly Installment: {round(monthly_installment, 2)}") # 2 for two digit in after point in answer