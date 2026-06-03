nums=[1,2,3,2,1]

left=0
right=len(nums)-1
is_palindrome=True
while left<right:
    if nums[left]!=nums[right]:
        is_palindrome=False
        break
    left+=1
    right-=1
if is_palindrome:
    print(nums,"is palindrome")
else:
    print(nums,"is not palindrome")
