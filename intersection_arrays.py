# Problem: Given two sorted array of sizes m and n
# in which all elements are distinct. Find the 
# common elements between them
# Constraints: in O(m+n) complexity.

def inr(z):
  return z+1

def intersectionArrays(x, y, m, n):
  i, j = 0, 0
  while i<m and j<n:
    #print(i, j)
    if(x[i] == y[j]):
      print(x[i])
      i = inr(i)
      j = inr(j)
    elif(x[i] < y[j]):
      i = inr(i)
    else:
      j = inr[j]
    
list_a = [1, 2, 3, 4, 5]
list_b = [2, 3, 5, 6]
intersectionArrays(list_a, list_b, len(list_a), len(list_b))
