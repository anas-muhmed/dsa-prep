#eg: input--6  -- 1+2+3=6  ..sum of perfect divisor = 6

def perfect(n):
    
    for current in range(1,n):
      sum=0
      for i in range(1,current):
          if current%i==0:
              sum+=i
      if sum==current:
          print(f"{current} is perfect")
      else:
          print(f"{current}not perfect")

perfect(20)