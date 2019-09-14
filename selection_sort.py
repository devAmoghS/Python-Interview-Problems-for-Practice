# A simple implementation of Selection Sort

def selectionSort(arr):
  i = 0
  while i < len(arr):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
        
    arr[i], arr[min_index] = arr[min_index], arr[i]
    i = i + 1
  
  return arr

arr = [2, 6, 1, 5, 3, 4]
res = selectionSort(arr)
print(res)
      
