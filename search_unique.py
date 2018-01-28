# Problem: Given a sorted array in which all elements
# appear twice (one after one) and one element
# appears only once. Find that element
# Constraints: in O(log n) complexity.
def searchUnique(arr, low, high):
  # Base Cases
  # 1. low is greater than high
  # 2. Array with single element
  if(low>high):
    return None
  if(low == high):
    return arr[low]
  # Find the middle element
  mid = low + (high-low)//2
  # if the middle element lies at even place,
  # check i and i+1, if they are same, go to right else left
  if(mid%2 == 0):
    if(arr[mid] == arr[mid+1]):
      return searchUnique(arr, mid+2, high)
    else:
      return searchUnique(arr, low, mid)
  # if the middle element lies at odd place,
  # check i-1 and i, if they are same, go to right else left
  # Replace mid by mid-1 for above block
  else:
    if(arr[mid-1] == arr[mid]):
      return searchUnique(arr, mid+1, high)
    else:
      return searchUnique(arr, low, mid-1)
    
array = [ 1, 1, 2, 4, 4, 5, 5, 6, 6 ]
result = searchUnique(array, 0, len(array)-1)
print(result)
# Result: 2
