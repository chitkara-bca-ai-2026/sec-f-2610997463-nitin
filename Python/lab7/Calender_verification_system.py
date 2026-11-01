#  Calendar Verification System

print("========================================")
print("   CALENDAR VERIFICATION SYSTEM")
print("========================================")

# year input in integer
year = int(input("Enter year: ")) 

if year <= 0: # if year 0 or negative than invalid
    print("Error: Year must be a positive integer greater than 0.")
    exit() # exit from program


is_leap = False 
reason = "" # for reason store

if year % 100 == 0: # if century year
    if year % 400 == 0: # it must be divide by 400
        is_leap = True
        reason = "Century year divisible by 400"
    else:
        is_leap = False
        reason = "Century year not divisible by 400"
else: # agar non-century year hai
    if year % 4 == 0: # must be divide from 4
        is_leap = True
        reason = "Divisible by 4 and not a century year"
    else:
        is_leap = False
        reason = "Not divisible by 4"

if is_leap: # calender if  leap year
    feb_days = 29
    total_days = 366
    status = "LEAP YEAR"
else: # a common year
    feb_days = 28
    total_days = 365
    status = "COMMON YEAR"

# result
print("\n----------------------------------------")
print(f"Year: {year}")
print(f"Status: {status}")
print(f"Days in Year: {total_days} days")
print(f"Days in February: {feb_days} days")
print(f"Reason: {reason}")
print("----------------------------------------")