from math import sqrt

def get_prime_factors(num):
  factors = []

  # get all the 2's
  while num % 2 == 0:
    factors.append(2)
    num = num / 2
  
  # check for other prime factors
  # sqrt is used to reduce the range by log(n)
  # step size of 2 to avoid checking with even numbers
  for i in range(3, int(sqrt(num))+1, 2):
    while num % i == 0:
      # print(num, i)
      factors.append(i)
      num = num / i
  
  # num is now the last prime number
  if num > 2:
    factors.append(int(num))

  return factors


n = int(input("Enter the number: "))
result = get_prime_factors(n)

print("The factors of {n} are {result}".format(n=n, result=result))

# Enter the number: 1081310109
# The factors of 1081310109 are [3, 11, 17, 23, 181, 463]
