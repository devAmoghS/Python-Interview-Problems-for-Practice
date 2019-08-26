# using factorial, reduced the time complexity
# of program from O(2^N) to O(N)


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def computeCoefficient(col, row):
    return factorial(row) // (factorial(col) * factorial(row - col))


# Recusrive method to create the series
def computePascal(col, row):
    if col == row or col == 0:
        return 1
    else:
        return computeCoefficient(col, row)


# Method to create the triangle for `N` row
def printTriangle(num):
    for r in range(num):
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
