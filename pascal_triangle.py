# Recusrive method to create the series
def computePascal(col, row):
    # There are three things to compute
    # 1. Left edge: col is 0
    # 2. Right edge: col is same as row
    if col == row or col == 0:
        return 1
    # 3. any other cell: col-1 + col of the previous row
    else:
        return computePascal(col - 1, row - 1) + computePascal(col, row - 1)


# Method to create the triangle for `N` row
def printTriangle(num):
    for r in range(num):
        # upon observation, we can deduce the relation
        # num_cols = num_rows + 1
        for c in range(r + 1):
            print(str(computePascal(c, r)), end=" ")
        print("\n")


printTriangle(10)
"""
Output:
1 

1 1 

1 2 1 

1 3 3 1 

1 4 6 4 1 

1 5 10 10 5 1 

1 6 15 20 15 6 1 

1 7 21 35 35 21 7 1 

1 8 28 56 70 56 28 8 1 

1 9 36 84 126 126 84 36 9 1 
"""
