def product_pair(arr, x):
    arr_sorted = sorted(arr)

    for i in range(0, len(arr_sorted)):
        sub_array = arr_sorted[i + 1 :]
        if x // arr_sorted[i] in sub_array:
            return True

    return False


arr = [10, 20, 9, 40]
x = 400

res = product_pair(arr, x)
print(res)
