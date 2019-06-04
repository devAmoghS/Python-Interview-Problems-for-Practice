# Given an input string, it gives the 
# first non repeating character in it
# There are two implementations below
# 1. has less space complexity
# 2. has less time complexity

def first_non_repeating(input_string):
  frequency = dict()
  flag = None

  for char in input_string:
    if char in frequency.keys():
      frequency[char] += 1
    else:
      frequency[char] = 0

  for char in input_string:
    if frequency[char] == 0:
      flag = char
      break

  return flag

# lesser time complexity
# more space complexity
# obvious space-time trade-off
def first_non_repeating_v2(input_string):
  
  flag = None
  repeating = []
  non_repeating = []

  for char in input_string:
    if char in non_repeating:
      non_repeating.remove(char)
      repeating.append(char)
    else:
      non_repeating.append(char)
  
  if len(non_repeating) == 0:
    pass
  else:
    flag = non_repeating[0]
  
  return flag
      

result = first_non_repeating("djebdedbekfrnkfnduwbdwkd")
print(result)   # j

result = first_non_repeating("aabbcc")
print(result)   # None
