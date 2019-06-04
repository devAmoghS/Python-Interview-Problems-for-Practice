# Check if two strings are anagrams of each other

def anagramise(word):
  d = dict()

  for char in word:
    if char not in d.keys():
      d[char] = 1
    else:
      d[char] += 1
  
  return d

def is_anagram(str1, str2):
  return anagramise(str1) == anagramise(str2)

result = is_anagram("hello", "billion")
print(result)  # False
