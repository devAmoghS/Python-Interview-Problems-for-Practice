# Problem: Given a list of positive and negative numbers, find the maximum subarray sum.
# Constraint: Solve it in O(n)

# Solution: Use two variables to hold sums
# a. overall sum -- initialize to first element
# b. partial sum -- initialize to first element
# Traverse over the whole array
# If the current element is greater than partial sum, swap the partial sum with the current element
# If the partial sum is greater than overall sum, swap overall with partial sum
# the overall sum will be the contiguous subarray with the largest sum

def maxSubArraySum(arr):
  max_so_far = arr[0]
  current_max = arr[0]

  for i in range(1,len(arr)):
    current_max = max(arr[i], current_max + arr[i])
    max_so_far = max(max_so_far, current_max)
  
  return max_so_far

sampleArr = [-2, -3, 4, -1, -2, 1, 5, -3]

solution = maxSubArraySum(sampleArr)
print(solution)
