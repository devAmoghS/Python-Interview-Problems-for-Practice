# Given an array of integers we need to move 
# all the zeroes to the end and maintain the 
# order of rest of the elements. Needless to 
# say it should be an in-place solution

def move_zero_to_end(arr):
  count = 0
  
  for i in arr:
    if i != 0:
      arr[count] = i
      count = count + 1
  
  for i in range(count, len(arr)):
    arr[i] = 0

  return arr




array = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
res = move_zero_to_end(array)
print(res)
