def merge_sort(array):
    # derive the mid-point
    if len(array) > 1:
        mid = len(array) // 2

        # create the temp sub-arrays
        LEFT = array[:mid]
        RIGHT = array[mid:]

        # sort the first and second halves
        merge_sort(LEFT)
        merge_sort(RIGHT)

        # begin addig elements in sorted order
        i, j, k = 0, 0, 1

        while i < len(LEFT) and j < len(RIGHT):
            if LEFT[i] < RIGHT[j]:
                array[k] = LEFT[i]
                i += 1
            else:
                array[k] = RIGHT[j]
                j += 1
            k += 1

        # copy the remaining data
        while i < len(LEFT):
            array[k] = LEFT[i]
            i += 1
            k += 1

        while j < len(RIGHT):
            array[k] = RIGHT[j]
            j += 1
            k += 1


arr = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort(arr)
print(arr)
