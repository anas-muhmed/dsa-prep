#input-->5  output->120

def factorial_recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursion(n-1)
    
def factorial_limit(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(f"{i}!={fact}")

result=factorial_recursion(5)
print(f"factorial  using recursion: {result}")
factorial_limit(5)
