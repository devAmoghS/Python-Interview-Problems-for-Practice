# Let all odd numbers come before even numbers, 
# and sort the odd numbers in ascending order and 
# even numbers in descending order. 
# For example, the string '1982376455' becomes '1355798642'

def oddAscEvenDesc(inputStr):
  oddSubstr = ''
  evenSubstr = ''

  for char in inputStr:
    if int(char) % 2 == 0:
      evenSubstr += char
    else:
      oddSubstr += char
  
  temp = sorted(oddSubstr) + sorted(evenSubstr, reverse=True)

  return "".join(temp)

x = "978231456"
y = oddAscEvenDesc(x)
print(y)
