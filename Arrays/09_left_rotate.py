#[1,2,3,4,5]
#Rotate by 2 --> [3,4,5,1,2]
def left_rotate(nums, d):

    d = d % len(nums)

    return nums[d:] + nums[:d]

nums = [1,2,3,4,5]

res = left_rotate(nums, 2)

print(res)