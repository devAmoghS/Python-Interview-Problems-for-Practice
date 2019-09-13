# Given an array of integers, write a function that 
# returns true if there is a triplet (a, b, c) that 
# satisfies a^2 + b^2 = c^2.

def findPythagorasTriplet(arr, n):
  # convert the array to squares
  for i in range(0, n):
    arr[i] = arr[i] * arr[i]
  
  # sort the array
  arr.sort()

  # use meet in the middle to find the pair (a,b)
  for i in range(n-1, 1, -1):
    j = 0
    k = i-1

    while (j < k):
      # a pair is found
      if (arr[j] + arr[k]) == arr[i]:
        return True
      else:
        if (arr[j] + arr[k]) < arr[i]:
          j = j + 1
        else:
          k = k - 1

  return False

ar = [3, 1, 4, 6, 5] 
ar_size = len(ar) 
if(findPythagorasTriplet(ar, ar_size)): 
    print("Yes") 
else: 
    print("No")  
