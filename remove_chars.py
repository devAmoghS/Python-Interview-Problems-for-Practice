# Write an efficient function that deletes characters from an ASCII 
# string where any character existing in remove must be deleted from 
# str. For example, given a str of "Battle of the Vowels: Hawaii vs. 
# Grozny" and a remove of "aeiou", the function should transform str
# to “Bttl f th Vwls: Hw vs. Grzny”.

def removeChars(main_string, remove_string):
  result = ''
  for char in main_string:
    if char not in remove_string:
      result+=char
  return result
  
given_input = "Battle of the Vowels: Hawaii vs. Grozny"
vowels = "aeiou"
print(removeChars(given_input, vowels))
