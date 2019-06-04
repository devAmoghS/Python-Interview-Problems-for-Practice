# Given a string, return True if it
# is a numeric data type, False otherwise

def is_numeric(input_str):

  data_types = [int, float, complex,
  lambda T: int(T, 2), # binary
  lambda T: int(T, 8), # octal
  lambda T: int(T, 16) # hex
  ]

  for dtype in data_types:
    try:
      dtype(input_str)
      return True
    except ValueError:
      pass
  return False

tests = [
    '0', '0.', '00', '123', '0123', '+123', '-123', '-123.', '-123e-4', '-.8E-04',
    '0.123', '(5)', '-123+4.5j', '0b0101', ' +0B101 ', '0o123', '-0xABC', '0x1a1',
    '12.5%', '1/2', '½', '3¼', 'π', 'Ⅻ', '1,000,000', '1 000', '- 001.20e+02', 
    'NaN', 'inf', '-Infinity']
 
for s in tests:
    print(s,"---",is_numeric(s))
    
"""
OUTPUT:

0 --- True
0. --- True
00 --- True
123 --- True
0123 --- True
+123 --- True
-123 --- True
-123. --- True
-123e-4 --- True
-.8E-04 --- True
0.123 --- True
(5) --- True
-123+4.5j --- True
0b0101 --- True
 +0B101  --- True
0o123 --- True
-0xABC --- True
0x1a1 --- True
12.5% --- False
1/2 --- False
½ --- False
3¼ --- False
π --- False
Ⅻ --- False
1,000,000 --- False
1 000 --- False
- 001.20e+02 --- False
NaN --- True
inf --- True
-Infinity --- True
"""
