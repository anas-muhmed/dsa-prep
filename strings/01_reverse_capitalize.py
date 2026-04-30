s=input("enter the string :")    #hello world->olleH ldorW

words=s.split()
result=[]

for word in words:
    r_word=word[::-1]
    final_word=r_word[:-1]+r_word[-1].upper()+" "
    result.append(final_word)
print("".join(result))