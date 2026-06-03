#12345 → 5 digits
num=int(input("enter the number: "))
count=0
while num>0:
     count+=1
     num//=10
print("count is ",count)