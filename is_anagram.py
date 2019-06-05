# Check if two strings are anagrams of each other

def is_anagram(str1, str2):
  return str1 == str2[::-1]

result = is_anagram("hello", "billion")
print(result)  # False
