s=input("enter the string: ")
seen=set()
result=[]
for char in s:
    if char not in seen:
        seen.append(char)
        result.append(char)
print("".join(seen))
