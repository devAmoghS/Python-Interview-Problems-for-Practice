def most_common(str_a, str_b):
  return set(str_a) & set(str_b)

result = most_common("NAINA", "RENNE")
print(result) # {N}

def get_freq(str):
  freq_dict = {}
  for char in str.split():
    if char not in freq_dict.keys():
      freq_dict[char] = 1
    else:
      freq_dict[char] += 1
      
  return freq_dict

result = get_freq("Amogh loves to eat apple and mango. His sister also loves eating apple and mango")
print(result)
# {'Amogh': 1, 'loves': 2, 'to': 1, 'eat': 1, 'apple': 2, 'and': 2, 'mango.': 1, 'His': 1, 'sister': 1, 'also': 1, 'eating': 1, 'mango': 1}



def is_prime(num):
  flag = 1

  for i in range(2, num//2):
    if num % i == 0:
      flag = 0
      break

  if flag == 0:
    print(f"{num} is not prime...")
  else:
    print(f"{num} is prime...")

is_prime(7919) # 7919 is prime


def fibo_iter(n_terms):
  first, second = 0, 1
  for i in range(0, n_terms):
    if i <= 1:
      result = i
    else:
      result = first + second
      first = second
      second = result
    print(result, end=' ')

fibo_iter(5) # 0 1 1 2 3

def fibo_recur(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo_recur(n-1) + fibo_recur(n-2)


for i in range(0, 10):
  print(fibo_recur(i), end=' ') # 0 1 1 2 3 5 8 13 21 34
