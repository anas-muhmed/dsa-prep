#input-->[1,2,4,5]
#missing-->3
#gauss eq-->n*(n+1)//2
nums=list(map(int,input("Enter the numbers: ").split()))
n=len(nums)+1
expected_sum=n*(n+1)//2
actual_sum=sum(nums)
missing=expected_sum-actual_sum
print("Missing number is -->",missing)
