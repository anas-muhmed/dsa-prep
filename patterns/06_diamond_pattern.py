n=int(input("Enter the rows: "))

for i in range(1,n+1):
    space=n-i
    stars=2*i-1
    print(" " * space + "*" * stars)
for i in range(n-1,0,-1):
    space=n-i
    stars=2*i-1
    print(" " * space +"*" * stars)