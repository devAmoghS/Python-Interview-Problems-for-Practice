# Write a program to check if a 
# number is a palindrome or not

def is_num_palindrome(num):
  temp = str(num)
  i = 0
  j = len(temp) - 1

  while j > i:
    print(temp[i], temp[j])
    if temp[i] == temp[j]:
      i = i + 1
      j = j - 1
    else:
      return False
  return True

n = 3456543
res = is_num_palindrome(n)
print(res)
