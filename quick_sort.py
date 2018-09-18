def swap(a, b):
  temp = a
  a = b
  b = temp

def quick_sort(array):
  quick_sort_helper(array, 0, len(array)-1)

def quick_sort_helper(arr, first, last):
  if first < last:
    split_point = partition(arr, first, last)

    quick_sort_helper(arr, first, split_point - 1)
    quick_sort_helper(arr, split_point + 1, last)

def partition(arr, first, last):
  pivot = arr[first]

  left = first + 1
  right = last

  done = False

  while not done:
    
    # move left and right pointers to locate split_point
    while left <= right and arr[left] <= pivot:
      left += 1
    while arr[right] >= pivot and right >= left:
      right -= 1

    # when both pointers cross each other
    # we have located the split_point
    if right < left:
      done = True
    else:
      # swap the left and right elements
      swap(arr[left], arr[right])

  # swap the first and right elements
  swap(arr[first], arr[right])

  return right

  array = [54,26,93,17,77,31,44,55,20]
  quick_sort(array)
  print(array)
