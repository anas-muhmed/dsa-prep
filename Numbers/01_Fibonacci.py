#input--->5  output-->0,1,1,2,3

num=int(input("Enter the Number: "))
a,b=0,1
while num>0:
    print(a,end=" ")
    a,b=b,a+b
    num-=1