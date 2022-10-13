# Problem: Given an array arr[] of n integers,
# the integers can be positive, negative or 0
# return the sign of the product of the elements
#  1 : positive
# -1 : negative
#  0 : zero


def getSignOfProduct(array):
  
  sign = 1
  
  for num in array:
    
    if num == 0:
      return 0
    
    if num < 0:
      sign = -1 * sign
  
  return sign


arr = [10, 45, -9, 3, -4, -5, 7, 32 , 0, 12 , 45, -1]
res = getSignOfProduct(arr)
print(arr, res)

# Result: [10, 45, -9, 3, -4, -5, 7, 32, 0, 12, 45, -1] 0
