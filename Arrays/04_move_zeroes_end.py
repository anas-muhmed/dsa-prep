#input---[0,1,0,3,12]  output-->[1,3,12,0,0]
def move_zeroes(nums):
    # 'write' pointer tracks where the next non-zero element should go
    write = 0
    
    # 'read' pointer scans through the entire array
    for read in range(len(nums)):
        # If we find a non-zero element, swap it with the write pointer position
        if nums[read] != 0:
            nums[write],nums[read] = nums[read],nums[write]
            write += 1
            
    return nums

# Test the function
array = [0, 1, 0, 3, 12]
print(move_zeroes(array))
