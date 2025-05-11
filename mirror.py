# Input number of rows
n = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, n + 1):
    # Print spaces first (n - i)
    for j in range(n - i):
        print(" ", end="")
    # Then print stars (i)
    for k in range(i):
        print("*", end="")
    # Move to the next line
    print()
