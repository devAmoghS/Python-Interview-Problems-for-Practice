# Write a program to convert interger to Roman Representation
def convertIntegerToRomanNum(input_num):

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

  while input_num > 0:
    # if input_num//number_list[i] > 0 , then we will get a string appended
    # else it will continue the loop
    for _ in range(input_num//number_list[i]):
      result_str = result_str + symbol_list[i]
      input_num = input_num - number_list[i]
    i = i + 1
  return result_str

roman = convertIntegerToRomanNum(289)
print(roman)

# ===============
# Explaination:
# ===============
# 289
# 289//1000   --> 0, i=1
# 289//900    --> 0, i=2
# 289//500    --> 0, i=3
# 289//400    --> 0, i=4
# 289//100    --> 2, then i=4, result_str = 'C',        input_num = 189
# 189//100    --> 1, then i=4, result_str='CC',         input_num = 89
# 89//100     --> 0, then i=5
# 89//50      --> 1, then i=6, result_str='CCL',        input_num= 39
# 39//50      --> 0, then i=6
# 39//40      --> 0, then i=7
# 39//10      --> 3, then i=8, result_str='CCLX',       input_num=29
# 29//10      --> 3, then i=8, result_str='CCLXX',      input_num=19
# 19//10      --> 3, then i=8, result_str='CCLXXX',     input_num=9
# 9//10       --> 0, then i=9
# 9//9        --> 1, then i=9, result_str='CCLXXXIX',   input_num=0
# EXIT
