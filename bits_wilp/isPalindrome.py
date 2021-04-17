def isPalindrome(str):
  result = False
  
  if str == str[::-1]:
    result = True
    
  return result   

print("Please enter a string: ")
x = input()
flag = isPalindrome(x)

if flag:
  print(x, "is a Palindrome")
else:
  print(x, "is NOT a Palindrome")
