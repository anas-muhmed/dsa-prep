nums=[1,2,2,3,1,1]
freq={}
for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

for key,value in freq.items():
    print(f"{key}={value}")         
