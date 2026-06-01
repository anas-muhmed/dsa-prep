#input-->5   output-->prime  "Number is divisble by 1 and itself"

def prime_number(n):
    if n<=1:
       print("not prime")
    else:
        is_prime=True
        for i in range(2,n):
            if n%i==0:
                is_prime=False
                break
            
        if is_prime:
            print("prime number")
        else:
            print ("not prime")


def primeNumberUptoLimit(n):
    if n<=1:
        print("number is not prime")
    else:
        for current in range(2,n+1):
            is_prime=True
            for i in range(2,current):
                if current%i==0:
                    is_prime=False
                    break
            if is_prime:
                print(current)

num=int(input("enter the number : "))
prime_number(num)
primeNumberUptoLimit(num)