num=int(input("Enter the number:"))

if num<=0:
    print("not power of 2")
else:
    while num%2==0:
        num//=2

    if num==1:
       print("power of 2")
    else:
       print("not power of two")