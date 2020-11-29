# Write a program to convert interger to Roman Representation
def convertIntegerToRomanNum(inputNumber):

  number_list = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
  ]

  symbol_list = [
    'M', 'CM', 'D',  'CD',
    'C',  'XC', 'L', 'XL',
    'X', 'IX',  'V', 'IV',
    'I'
  ]

  result_str = ''
  i = 0

  while inputNumber > 0:
    for _ in range(inputNumber//number_list[i]):
      result_str = result_str + symbol_list[i]
      inputNumber = inputNumber - number_list[i]
    i = i + 1
  return result_str

roman = convertIntegerToRomanNum(289)
print(roman)
