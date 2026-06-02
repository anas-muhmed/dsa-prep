#eg:153---> 1 cube+ 5 cube+ 3 cube =153

def armstrong(n):
    temp=n
    res=0
    while temp>0:
        num=temp%10
        res+=num**len(str(n))
        temp//=10
    if res==n:
        print("armstrong")
    else:
        print("not armstrong")

nums=int(input("Enter the number:"))
armstrong(nums)