def computeCoeff(row, col):
  """
  This method computes the Binomial coefficient for each point in the Pascal Triangle
  """
  if col == 0 or row == col:
    return 1 # for the corners of each row
  else:
    return computeCoeff(row-1, col) + computeCoeff(row-1, col-1) # take the numbers in previous row same column and one column left of that number

def printTriangle(n):
  """
  This method prints the Pascal triangle with `n` rows
  """
  for r in range(n):
    for c in range(r+1):
      print(computeCoeff(r,c), end=' ')
    print('\n')

printTriangle(10)

# Output
"""
1 

1 1 

1 2 1 

1 3 3 1 

1 4 6 4 1 

1 5 10 10 5 1 

1 6 15 20 15 6 1 

1 7 21 35 35 21 7 1 

1 8 28 56 70 56 28 8 1 

1 9 36 84 126 126 84 36 9 1 
"""
