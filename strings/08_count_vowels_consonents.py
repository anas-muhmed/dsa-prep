s=input(("enter the string: "))
vowels='aeiouAEIOU'
v_count=0
c_count=0
s_count=0
for char in s:
    if char in vowels:
        v_count+=1
    elif char.isalpha():
        c_count+=1
    elif char.isspace():
        s_count+=1
print(f"vowel count{v_count}")
print(f"consonent count{c_count}")
print(f"space count{s_count}")