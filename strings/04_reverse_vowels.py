#vowel reverse
#input->hello world   ouput->hollo werld
s=input("enter the string:")

vowels=aeiouAEIOU
position=[]
for i in range(len(s)):
    if s[i] in vowels:
        position.append(i)
vowel_char=[]
for i in position:
    vowel_char.append(word[i])

vowel_char[::-1]
word_list=[]=s

for i in range(len(position)):
  word_list[position[i]]=vowel_char[i]
print("".join(word_list))
