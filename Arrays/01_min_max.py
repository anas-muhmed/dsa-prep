#input-->[4, 7, 1, 9, 2] output--->min:1 max:9
#method 1:sorted
#method 2:using max and min method
#method 3:

nums = [2, 9, 1, 7, 4]

min_num = nums[0]
max_num = nums[0]

for x in nums[1:]:

    if x < min_num:
        min_num = x

    if x > max_num:
        max_num = x

print("Maximum number is:", max_num)
print("Minimum number is:", min_num)