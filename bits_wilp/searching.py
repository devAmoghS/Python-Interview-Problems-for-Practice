
# Searching: Given a sorted array arr[] of n elements, write a
# function to search a given element x in arr[]. Do it using linear
# and binary search techniques.

def linear_search(arr, elem):
  for i in range(0,len(arr)):
    if arr[i] == elem:
      print("{elem} found at {index} !".format(elem=elem, index=i))
      return
  print("{elem} not found in given sequence".format(elem=elem))

def binary_search(arr, elem, l, r):
  try:
    mid = (l + r) // 2

    if elem == arr[mid]:
      print("{elem} found at {index} !".format(elem=elem, index=mid))
      return
    elif elem > arr[mid]:
      binary_search(arr, elem, l=mid+1, r=r)
    elif elem < arr[mid]:
      binary_search(arr, elem, l=l, r=mid-1)

  except RecursionError as e:
    print("{elem} not found in given sequence".format(elem=elem))
    print(e)


arr = list(map(int, input("Enter numbers seperated by space. Press ENTER to exit: ").split()))
arr.sort()
print("Given sequence is :")
print(arr)

elem = int(input("Enter element to be searched: "))
choice = int(input("Choose search method: \n 1. Linear Search \n 2. Binary Search \n"))

if choice == 1:
  linear_search(arr, elem)
elif choice == 2:
  binary_search(arr, elem, l=0, r=len(arr)-1)
else:
  print("Error: Please enter a valid choice !")  
