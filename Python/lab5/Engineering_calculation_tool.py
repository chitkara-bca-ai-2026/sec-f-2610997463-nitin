#  Engineering Calculation Tool



import math # from math module we  can use  isme pow, sqrt, ceil, floor fxns.

print("========================================")
print("   ENGINEERING CALCULATION TOOL")
print("========================================")

# input enter
num = float(input("Enter a numerical value: ")) 
exponent = float(input("Enter an exponent: ")) 
decimal_val = float(input("Enter a decimal measurement: ")) 

# by using using import math module
power_val = math.pow(num, exponent) # pow() se power nikalna (num^exponent)
sqrt_val = math.sqrt(num)             # sqrt(), find square root nikalna
ceil_val = math.ceil(decimal_val)        # ceil(),  next (uper) round value
floor_val = math.floor(decimal_val)       # floor(), previous (lower) round value

# display all results
print("\n--- Results ---")
print(f"Value            : {num}")
print(f"Exponent         : {exponent}")
print(f"Power (pow)      : {power_val}")
print(f"Square Root (sqrt) : {sqrt_val}")
print(f"Decimal Value    : {decimal_val}")
print(f"Ceil Value       : {ceil_val}")
print(f"Floor Value      : {floor_val}")
print("========================================")

