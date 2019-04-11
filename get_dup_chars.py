# Print duplicate characters in a string

def get_dup_chars(input_str):
  dedupe_str = ''
  dup_chars = []

  for char in input_str:
    if char not in dedupe_str:
      dedupe_str += char
    else:
      dup_chars.append(char)

  return dup_chars

result = get_dup_chars("zmaxxazkgv")
print(result)  # ['x', 'a', 'z']
