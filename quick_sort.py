def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)


def quick_sort_helper(arr, first, last):
    if first < last:
        pi = partition(arr, first, last)

        quick_sort_helper(arr, first, pi-1)
        quick_sort_helper(arr, pi+1, last)


def partition(arr, first, last):
    pivot = arr[first]

    left = first+1
    right = last

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1

        while arr[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[first], arr[right] = arr[right], arr[first]

    return right


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist)
print(alist)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
