# Given a string, check if it only contains digits

def is_digit(input_str):
  digits = dict()

  for char in input_str:
    if char in digits:
      digits[char] += 1
    else:
      digits[char] = 1
  
  if sum(digits.values()) == len(input_str):
    return True
  else:
    return False

result = is_digit("095357973590759530")
print(result)  # True
