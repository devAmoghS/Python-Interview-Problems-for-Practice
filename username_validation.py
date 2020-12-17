# Have the function UsernameValidation(`str`) take the `str` parameter being passed and determine if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

#If the username is valid then your program should return the string `true`, otherwise return the string `false`.

def UsernameValidation(strParam):

  # username is between 4 and 25 characters
  if len(strParam) <= 25 and len(strParam) >= 4:
    flag1 = True
  else:
    flag1 = False

  # start with a letter
  if str(strParam[0]).isalpha():
    flag2 = True
  else:
    flag2 = False

  # contains only letters, numbers and underscore
  valid_grammar = "abcdefghijklmnopqrstuvwxyz0123456789_"

  for char in strParam:
    if str(char).isalpha() == False:
      if char in valid_grammar:
        flag3 = True
      else:
        flag3 = False

    else:
      if str.lower(char) in valid_grammar:
        flag3 = True
      else:
        flag3 = False    


  # can't end with an underscore
  if str(strParam[-1]) != '_':
    flag4 = True
  else:
    flag4 = False

  final_output = flag1 and flag2 and flag3 and flag4

  # code goes here
  return final_output

# keep this function call here
TC1 = "aa_"
TC2 = "u__hello_world123"

print(TC1, UsernameValidation(TC1))
print(TC2, UsernameValidation(TC2))
