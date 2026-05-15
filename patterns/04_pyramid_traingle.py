row = int(input("Enter number of rows: "))

if row <= 0:
    print("Invalid input")
else:
    for i in range(1, row + 1):
        spaces = row - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)