# Check if two strings are anagrams of each other


from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


result = is_anagram("hello", "billion")
print(result)  # False

result = is_anagram("million", "million")
print(result)  # True
