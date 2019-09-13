# Problem: Given an array arr[] of n integers,
# construct a Product Array prod[] (of same size)
# such that prod[i] is equal to the product of all
# the elements of arr[] except arr[i].

# Constraints: Solve it without division operator and in O(n)


def computeProductArray(array, size):
    # initialize three arrays of the same size as given array
    # Left: will hold the product of all the elements to the left
    # Right: will hold the product of all the elements to the right
    # Product: contains the product value for current element

    prod = [1] * size
    left = [1] * size
    right = [1] * size

    for i in range(1, size):
        left[i] = array[i - 1] * left[i - 1]
    # decreasing loop in Python {start, end, step(-ve)}
    # equivalent to (j=size-2; j>=0; j--)
    for j in range(size - 2, -1, -1):
        right[j] = array[j + 1] * right[j + 1]
    for k in range(0, size):
        prod[k] = left[k] * right[k]
    print(prod)


arr = [10, 3, 5, 6, 2]
computeProductArray(arr, len(arr))
# Result: [180, 600, 360, 300, 900]
