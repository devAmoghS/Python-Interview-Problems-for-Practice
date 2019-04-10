def remove_duplicates(arr):
  return list(dict.fromkeys(arr))

result = remove_duplicates([0,0,0,1,1,2,2,3,4,5])
print(result)   # [0, 1, 2, 3, 4, 5]
