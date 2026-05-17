

def is_anagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


#-----------------------------------------#
def is_anagram(s: str, t: str) -> bool:
    # Anagrams must have the exact same length
    if len(s) != len(t):
        return False
        
    count = {}
    
    # Count frequencies of characters in string 's'
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    # Subtract frequencies using characters in string 't'
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
        
    return True

# Example Usage
print(is_anagram("anagram", "nagaram"))  # Output: True
print(is_anagram("rat", "car"))          # Output: False
