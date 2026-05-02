rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Invalid input")
else:
    num = 1
    for row in range(1, rows + 1):
        for col in range(row):
            print(num, end=" ")
            num += 1
        print()
