# Write a function that computes the 
# list of the first 100 Fibonacci numbers

FIB_ARR = [0, 1]

def first_n_fibo(n):
  if n < 2:
    return FIB_ARR
  else:
    while len(FIB_ARR) < n:
      FIB_ARR.append(FIB_ARR[-1] + FIB_ARR[-2])
    return FIB_ARR


n = 10
arr = first_n_fibo(n)
print(arr)
