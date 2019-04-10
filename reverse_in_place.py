def reverse_in_place(arr):
  i = 0
  j = len(arr) - 1

  while i != j and i<j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1

  return arr

result = reverse_in_place([4, 12, 14, 16, 18])
print(result)
