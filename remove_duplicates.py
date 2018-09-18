def remove_duplicates(num_array):
  d = dict()
  for idx in range(0, len(num_array)):
    if num_array[idx] in d.keys():
      num_array[idx] = 0
    d[num_array[idx]] = 1
  dedupe_array = [n for n in num_array if n != 0]
  return dedupe_array

result = remove_duplicates([1, 1, 2, 2, 3, 4, 5])
print(result)   # [1, 2, 3, 4, 5]
