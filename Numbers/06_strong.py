# 145--->1!+4!+5!=145

def strong_number(n):
    sum=0
    
    temp=n
    while temp>0:
        fact=1
        digit=temp%10
        for i in range(1,digit+1):
            fact*=i
        factorial_sum+=fact
        temp//=10
    if factorial_sum==n:
        print("Strong Number ")
    else:
        print("Not  a Strong number")

        #-----------------------------------------------------------------------#
def strong_number_optimized(n):
    # Precomputed factorials for digits 0 to 9
    FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += FACTORIALS[digit]  # O(1) constant time lookup
        temp //= 10

    if total == n:
        print("Strong Number")
    else:
        print("Not Strong Number")

strong_number_optimized(145)

strong_number(145)
