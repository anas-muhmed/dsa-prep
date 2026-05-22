s = input("enter the string:")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# --- Modified Section ---
unique_count=0
found=False

for ch in s:
    if freq[ch]==1:
        unique_count+=1

        if unique_count==2:
            found=True
            print(f"The second non-repeating character is: {ch}")
            break

if not found:
    print("There is no second non-repeating character.")
