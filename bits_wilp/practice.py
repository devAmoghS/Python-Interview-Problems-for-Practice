def most_common(str_a, str_b):
  return set(str_a) & set(str_b)

result = most_common("NAINA", "RENNE")
print(result) # {N}

def get_freq(str):
  freq_dict = {}
  for char in str.split():
    if char not in freq_dict.keys():
      freq_dict[char] = 1
    else:
      freq_dict[char] += 1
      
  return freq_dict

result = get_freq("Amogh loves to eat apple and mango. His sister also loves eating apple and mango")
print(result)
# {'Amogh': 1, 'loves': 2, 'to': 1, 'eat': 1, 'apple': 2, 'and': 2, 'mango.': 1, 'His': 1, 'sister': 1, 'also': 1, 'eating': 1, 'mango': 1}
