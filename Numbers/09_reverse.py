#1234 → 4321
nums=int(input("Enter the Number: "))
reverse=0
while nums>0:
    digit=nums%10
    reverse=(reverse*10)+digit
    nums//=10
print("reversed number is:",reverse)