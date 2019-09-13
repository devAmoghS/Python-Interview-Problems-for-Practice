# Write an efficient program for 
# printing k largest elements in 
# an array. Elements in array can
# be in any order.
# Time Complexity: O(NlogN) + O(k)

def findKLargest(arr, k):
  arr.sort(reverse=True)
  for i in range(0, k):
    print(arr[i], end=" ")
    
arr = [1, 23, 12, 9, 30, 2, 50] 
k = 3
findKLargest(arr, k)
