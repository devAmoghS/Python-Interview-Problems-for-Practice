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
      

result = first_non_repeating("djebdedbekfrnkfnduwbdwkd")
print(result)   # j

result = first_non_repeating("aabbcc")
print(result)   # None
