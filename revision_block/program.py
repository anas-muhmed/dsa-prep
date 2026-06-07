def power_of_two():
    num=int(input("enter the input: "))
    if num<=0:
        print("not power of two")
    else:
        while num%2==0:
            num//=2
    if num==1:
        print("power of two")
    else:
        print("not power of two")


power_of_two()