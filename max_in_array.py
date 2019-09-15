def maxIndex(arr):
  max_index = 0
  for i in range(1, len(arr)):
    if arr[max_index] < arr[i]:
      max_index = i
  return max_index

arr = [4,5,6,7,8,1,2,11,12,13,3,9,10]
res = maxIndex(arr)
print("maximum element is", arr[res],"at index:", res)
