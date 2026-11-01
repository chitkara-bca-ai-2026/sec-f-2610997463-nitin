# Festival Decoration Designer

n = int(input("Enter the number of rows: "))    # input for how many rows needed

#  star triangle (rgt. angle)

print("Pattern 1: Star Triangle")
print("----------------------------------------")
for i in range(1, n + 1):   # for 1 to n range
    for j in range(i):       # Inner loop print stars in every row (i)
        print("*", end=" ")     # for print in same line
    print()   # to go in next line


# number triangle

print("\nPattern 2: Number Triangle")
print("----------------------------------------")
for i in range(1, n + 1): 
    for j in range(1, i + 1): 
        print(j, end=" ")
    print()


# inverted star triangle
print("\nPattern 3: Inverted Star Triangle")
print("----------------------------------------")
for i in range(n, 0, -1):     # reverse loop from n to 1
    for j in range(i):      # in every row (i)  stars
        print("*", end=" ")
    print()

# Pyramid
print("\nPattern 4: Pyramid")
print("----------------------------------------")
for i in range(1, n + 1): 
    #  print space to make pyramid at center
    for k in range(n - i):
        print(" ", end=" ")
    # stars print  using (2*i-1) formula
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

