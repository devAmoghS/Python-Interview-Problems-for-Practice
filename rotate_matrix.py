# Problem: Rotate a square matrix by
# 90 degree with O(1) extra space
def rotate_by_90(m):
  # unpacking arguments with zip(*) in reverse with [ : :-1]
  tuples = zip(*m[::-1])
  # flattening tuples to list with [list(i)]
  return [list(i) for i in tuples]
  
def makeMatrix(array, size):
  # validating size of matrix for given array
  if (size**2!=len(array)):
    return -1
  # make sub array of length size using array slicing  
  else:
    matrix = [array[i:i+size] for i in range(0, len(array), size)]
    return rotate_by_90(matrix)

arr = [1,2,3,4]
dimension = 2
result = makeMatrix(arr, dimension)
# Original Matrix: [[1, 2], [3, 4]]
# Result: [[3, 1], [4, 2]]
