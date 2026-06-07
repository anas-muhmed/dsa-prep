nums=[1,1,2,2,3]

#nums=list(set(nums))
#print(nums) 

write_idx=1
for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]:
        nums[write_idx]=nums[i]
        write_idx+=1

nums=nums[:write_idx]
print(nums)

#another solution
# dict.fromkeys() creates unique keys, then list() converts it back
#nums = list(dict.fromkeys(nums))