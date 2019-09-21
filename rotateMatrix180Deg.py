def rotateMatrixby90(ipMat, size):
  opMat = [[0 for i in range(size)] for j in range(size)]

  for i in range(size):
    for j in range(size):
      opMat[j][i] = ipMat[i][j]
  
  return opMat

def reverseMatrix(ipMat, size):
  opMat = [[0 for i in range(size)] for j in range(size)]
  for i in range(size):
    for j in range(size):
      opMat[abs(i-(size-1))][j] = ipMat[i][j]
  
  return opMat

def rotateMatrixby180(ipMat, size):
  mat_1 = rotateMatrixby90(ipMat, size)
  mat_2 = reverseMatrix(mat_1, len(mat_1))
  mat_3 = rotateMatrixby90(mat_2, len(mat_2))
  mat_4 = reverseMatrix(mat_3, len(mat_3))

  return mat_4

def printMatrix(ipMat, size):
  for i in range(size):
    for j in range(size):
      print(ipMat[i][j], end=" ")
    print('\n')

matA = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print("Original-Matrix" + '\n')
printMatrix(matA, len(matA))

print("Rotated-Matrix" + '\n')
rotatedMat = rotateMatrixby90(matA, len(matA))
printMatrix(rotatedMat, len(rotatedMat))

matB = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
reverseMat = reverseMatrix(matB, len(matB))
print("Reverse-Matrix" + '\n')
printMatrix(reverseMat, len(reverseMat))

print("Rotated-180-Matrix" + '\n')
rotatedMat180 = rotateMatrixby180(matA, len(matA))
printMatrix(rotatedMat180, len(rotatedMat180))
