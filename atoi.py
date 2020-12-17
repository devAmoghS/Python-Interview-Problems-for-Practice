# Convert the string "123" into 123, without using the built-api `int()`

# Startegy
# 1. loop through each digit
# 2. find the digit in range object of range(10)
# 3. once the number is found, add it in placeholder
# 4. Multiply each iteration by 10 (start with 0)

def atoi(inputStr):
  outputNum = 0
  for char in inputStr:
    for i in range(10):
      if str(i) == char:
        outputNum = outputNum * 10 + i
  return outputNum

x = "123"
y = atoi(x)
print(y)
