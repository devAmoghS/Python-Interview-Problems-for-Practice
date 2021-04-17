#  A simple implementation of bubble sort

def bubbleSort(arr):
  # travese the whole array
  for i in range(len(arr)):
    
    # last i elements are already in place
    for j in range(0, len(arr)-i-1):
      
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  
  return arr

# Approach 2: This algorithm will run for O(n^2) even if the array is
# already sorted. For avoiding this, we can check if elements are swapped
# in each pass. We will break the loop in case they are not

# Time Complexity: O(n^2) - Average or Worst Case; O(n) - Best case [Array is already sorted]

def bubbleSortOptimized(arr):
  for i in range(len(arr)):
    swapped = False
    
    for j in range(0, len(arr)-i-1):
      
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    
    # if no elements are swapped, break the loop
    if swapped == False:
      break
  
  return arr

if __name__ = "__main__":
  arr = [2, 6, 1, 5, 3, 4]
  res = bubbleSort(arr)
  print(res)
