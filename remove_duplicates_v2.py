def remove_duplicates_v2(arr):
  dedupe_arr = []

  for i in arr:
    if i not in dedupe_arr:
      dedupe_arr.append(i)
  
  return dedupe_arr

result = remove_duplicates([0,0,0,1,1,2,2,3,4,5])
print(result)
