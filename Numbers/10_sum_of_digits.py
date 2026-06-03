#1234 → 1+2+3+4 = 10
num=int(input("enter the number:"))

sum=0
while  num>0:
    digit=num%10
    sum+=digit
    num//=10
print(sum)