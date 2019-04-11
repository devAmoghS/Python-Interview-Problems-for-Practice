# Check if two strings are anagrams of each other

def is_anagram(str1, str2):

  if len(str1) == len(str2):
    for i in str1:
      if i in str2:
        pass
      else:
        return False
    return True
  else:
    return False

result = is_anagram("hello", "billion")
print(result)  # False
