#input--->5  output-->0,1,1,2,3

num=int(input("enter the number: "))
a,b=0,1
while num>0:
    print(a)
    a,b=b,a+b
    num-=1
