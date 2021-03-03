# Print numbers 1 to 100 without using any numbers or integers

# APPRAOCH
# Use Boolean values

ONE = str(int(True))
ZERO = str(int(False))
HUNDRED  = int(ONE + ZERO + ZERO)

for i in range(int(ONE), HUNDRED+1):
  print(i, end=', ')

# OUTPUT (Actual prints in the same line, line breaks given here for code clarity):

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
# 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
# 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
# 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
# 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
# 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
# 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
# 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
# 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
# 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,


# ALTERNATE APPROACH
# ORD (or "ordinal") function in python gives the ASCII
# (American Standard Code for information interchange) value 
# of characters ranging from 0-256 in 8 bits of memory which 
# is equal to a byte.

ONE = str(ord('b') - ord('a'))
ZERO = str(ord('a') - ord('a'))
HUNDRED  = int(ONE + ZERO + ZERO)

for i in range(int(ONE), HUNDRED+1):
  print(i, end=', ')
