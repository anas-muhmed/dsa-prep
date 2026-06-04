nums = [4,7,5,6,8,1]

largest = float('-inf')
second_largest = float('-inf')

for x in nums:

    if x > largest:
        second_largest = largest
        largest = x

    elif x > second_largest and x != largest:
        second_largest = x

if second_largest == float('-inf'):
    print("No second largest element")

else:
    print("Second largest:", second_largest)