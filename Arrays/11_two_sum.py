#nums = [2,7,11,15]
#target = 9
def two_sum(nums, target):
    # Map to store: { number_value : its_index }
    seen = {}
    
    for current_index, current_num in enumerate(nums):
        complement=target-current_num
        if complement in seen:
            return [seen[complement],current_index]
        seen[current_num]=current_index
nums=[2,7,11,15]
target=9
res=two_sum(nums,target)
print(res)