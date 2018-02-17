# Problem: Two strings of sizes m and n are given,
# we have to find how many characters need to be
# removed from both the string so that they become
# anagrams of each other

import string
letters = string.ascii_lowercase
CHARACTER_HASH = dict(zip(letters, [0]*len(letters)))

def mapLettersToHash(text_a):
  for char in text_a:
    if char in CHARACTER_HASH.keys():
      CHARACTER_HASH[char]+=1

def computeCommonLetters(text_b):
  common_letters = 0    
  for char in text_b:
    if CHARACTER_HASH[char] > 0:
      common_letters+=1
  return common_letters

def computeUncommonLetters(text_a, text_b, common_letters):
  return abs(len(text_a)+len(text_b)-(2*common_letters))

text_1 = "hello"
text_2 = "billion"

mapLettersToHash(text_1)
common = computeCommonLetters(text_2)
result = computeUncommonLetters(text_1, text_2, common)
print(result)    
