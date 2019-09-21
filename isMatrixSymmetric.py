def isMatrixSymmetric(mat, size):
  for i in range(size):
    for j in range(size):
      if mat[i][j] != mat[j][i]:
        break
        return False
  
  return True

ipMat = [[1,2,3],[2,4,5],[3,5,8]]
result = isMatrixSymmetric(ipMat, len(ipMat))
print(result)
