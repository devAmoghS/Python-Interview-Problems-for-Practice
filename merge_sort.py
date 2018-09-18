def merge_sort(array, left, right):
  # derive the mid-point
  if left < right:
    mid = (left+(right-1))//2
    # print("mid", mid)

    # sort the first and second halves
    merge_sort(array, left, mid)
    merge_sort(array, mid+1, right)
    # merge back
    merge(array, left, mid, right)

def merge(array, left, mid, right):
  # initialize sizes for the sub-arrays
  size_left = mid - left + 1
  # print("size_left", size_left)
  size_right = right - mid
  # print("size_right", size_right)

  # create the temp sub-arrays
  LEFT = [0] * (size_left)
  # print("LEFT", LEFT)
  RIGHT = [0] * (size_right)
  # print("RIGHT", RIGHT)

  # copy data to the sub-arrays
  for i in range(0, size_left):
    LEFT[i] = array[left + i]

  for j in range(0, size_right):
    RIGHT[j] = array[mid + 1 + j]

  # merge into original array
  i, j, k = 0, 0, 1

  while i < size_left and j < size_right:
    if LEFT[i] <= RIGHT[j]:
      array[k] = LEFT[i]
      i += 1
    else:
      array[k] = RIGHT[j]
      j += 1
    k += 1

arr = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort(arr, 0, len(arr))
