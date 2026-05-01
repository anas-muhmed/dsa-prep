#input aabbccd->d

s=input("enter the string:")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

found=False
for ch in s:
    if freq[ch]==1:
        found=True
        print(ch)
        break
if not found:
    print("no non repeating")