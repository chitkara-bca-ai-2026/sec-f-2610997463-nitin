# online account registration
username = input("Enter your username: ")
password = input("Enter your password: ")
print("=" * 40)
print("PASSWORD VALIDATION REPORT")
print("=" * 40)
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print()
print("--- Validation Rules ---")
has_digit = False
has_upper = False
for c in password:
    if c.isdigit():
        has_digit = True
    if c.isupper():
        has_upper = True
if len(password) >= 8:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
    check1 = True
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")
    check1 = False
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
if check1 and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("=" * 40)
