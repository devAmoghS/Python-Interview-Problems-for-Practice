# Remove duplicate characters from string

def remove_dup_chars(input_str):
  dedupe_str = ''

  for char in input_str:
    if char not in dedupe_str:
      dedupe_str += char

  return dedupe_str

result = remove_dup_chars("zmaxxazkgv")
print(result)  # zmaxxazkgv
