# Given a string, get it reversed using recursion

def recursive_reverse(input_str):
  if len(input_str) == 0:
    return ''
  else:
    return recursive_reverse(input_str[1:]) + input_str[0]

result = recursive_reverse("aabbcc")
print(result)  # ccbbaa
