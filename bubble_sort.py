#  A simple implementation of bubble sort

def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  
  return arr

arr = [2, 6, 1, 5, 3, 4]
res = bubbleSort(arr)
print(res)
