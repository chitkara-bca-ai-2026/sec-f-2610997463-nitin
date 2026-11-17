username = input("Enter your username: ")
password = input("Enter your password: ")
print("=" * 40)
print("PASSWORD VALIDATION REPORT")
print("=" * 40)
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print()
print("--- Validation Rules ---")
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
long_enough = len(password) >= 8
length_result = "PASS" if long_enough else "FAIL"
print(f"[{length_result}] Minimum 8 characters ({len(password)} characters)")

if has_digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if has_upper:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")
print()
print("--- Result ---")
if long_enough and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")
print("=" * 40)