#-- GCD=highest common divisor

a=int(input("Enter the first number:"))
b=int(input("Enter the Second number: "))

gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i

print("GCD =",gcd)

lcm=a*b//gcd  #common equation
print("LCM = ", lcm)

