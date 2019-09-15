def maxMinIndex(arr):
  
  max_index = 0
  min_index = 0

  # using two counters in single for loop
  for i, j in zip(range(1, len(arr)), range(1, len(arr))):
    if arr[max_index] < arr[i]:
      max_index = i
    if arr[min_index] > arr[i]:
      min_index = i

  return max_index, min_index

arr = [4,5,6,7,8,1,2,11,12,13,3,9,10]
res = maxMinIndex(arr)
print("maximum element is", arr[res[0]],"at index:", res[0])
print("minimum element is", arr[res[1]],"at index:", res[1])
