# Problem: Given two sorted array of sizes m and n
# in which all elements are distinct. Find the
# union between them
# Constraints: in O(m+n) complexity.

def unionArrays(x, y, m, n):
  union_arr = []

  for i in range(m):
    union_arr.append(x[i])
  
  for j in range(n):
    if y[j] not in union_arr:
      union_arr.append(y[j])

  print(union_arr)
  return

list_a = [1, 2, 3, 4, 5]
list_b = [2, 3, 5, 6]
unionArrays(list_a, list_b, len(list_a), len(list_b))
