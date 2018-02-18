# Problem: Given a string, find the first non-repeating 
# character in it. For example, if the input string is 
# “GeeksforGeeks”, then output should be ‘f’ and if input
# string is “GeeksQuiz”, then output should be ‘G’.

import string
letters = string.ascii_lowercase
CHARACTER_HASH = dict(zip(letters, [0]*len(letters)))

def mapLettersToHash(text_a):
  for char in text_a:
    if char in CHARACTER_HASH.keys():
      CHARACTER_HASH[char]+=1

def getFirstUniqueLetter(text_a):
  for char in text_a:
    if CHARACTER_HASH[char] == 1:
      return char

text_1 = "geeksquiz"

mapLettersToHash(text_1)
result = getFirstUniqueLetter(text_1)
print(result)    
