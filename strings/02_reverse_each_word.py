#python is fun ->nohtyp si nuf
s=(input("Enter the string:"))
result=[]
words=s.split()
for word in words:
    r=word[::-1]
    result.append(r)
print(" ".join(result))