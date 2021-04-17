def isAngstrom(n):
  result = False
  sum = 0
  order = len(n)

  for i in n:
    sum = sum + int(i)**order

  if sum == int(n):
    result = True
  return result   

print("Please enter a number: ")
num = input()
flag = isAngstrom(num)

if flag:
  print(num, "is an Angstrom number")
else:
  print(num, "is NOT an Angstrom number")
