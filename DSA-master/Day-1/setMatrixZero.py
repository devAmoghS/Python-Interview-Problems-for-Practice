# Set Matrix Zero
# Problem Statement: Given a matrix if an element in the matrix is 0 
# then you will have to set its entire column and row to 0 and then 
# return the matrix.

# Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

def getZeros(matrix, shape):
  """
  returns the location of zeros in the matrix
  as a list of tuples
  Time Complexity: O(M*N) where MxN is the shape of matrix
  """
  r,c = shape
  zeros = []
  for i in range(0,r):
    for j in range(0,c):
      if matrix[i][j] == 0:
        zeros.append((i,j))
  return zeros

def setZeros(matrix, shape, zeros):
  """
  returns the modified matrix
  Time complexity: O(M+N) where MxN is the shape of the matrix
  """
  r,c = shape

  for z in zeros:
    m,n = z
    for i in range(0,r):
      matrix[i][n] = 0

    for j in range(0,c):
      matrix[m][j] = 0

  return matrix

    

M = [[1,1,1],[1,0,1],[1,1,1]]
print(M)
res = getZeros(M, (3,3))
print(res)
sol = setZeros(M, (3,3), res)
print(sol)
