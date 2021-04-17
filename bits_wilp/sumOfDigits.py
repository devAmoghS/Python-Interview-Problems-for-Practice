def sumOfDigits(n):
  sum = 0
  while n > 0:
    rem = n % 10
    sum = sum + rem
    n = n // 10
  return sum   

print("Please enter a number: ")
num = int(input())
sod = sumOfDigits(num)
print("The sum of digits for", num, "is", sod)
