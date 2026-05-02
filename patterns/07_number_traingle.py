n = int(input("Enter the rows: "))

if n <= 0:
    print("Not possible")
else:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()