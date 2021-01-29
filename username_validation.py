# Have the function UsernameValidation(`str`) take the `str` parameter being passed and determine if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

#If the username is valid then your program should return the string `true`, otherwise return the string `false`.

def UsernameValidation(strParam):

  # username is between 4 and 25 characters
  if len(strParam) < 4 or len(strParam) > 25 :
    return False

  # start with a letter
  if not str(strParam[0]).isalpha():
    return False;

  # can't end with an underscore
  if str(strParam[-1] ) == '_':
    return False;

  # contains only letters, numbers and underscore
  valid_grammar = set('abcdefghijklmnopqrstuvwxyz0123456789_')

  for ch in strParam:
    if ch.lower() not in valid_grammar:
      return False;

  return True

# keep this function call here
TC1 = "aa_"
TC2 = "uaa__hello_worldW"

print(TC1, UsernameValidation(TC1))
print(TC2, UsernameValidation(TC2))
