def factorial(n):
  if n < 2:
    return 1
  else:
    return n * factorial(n-1)


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

# int division to avoid `float` output
ncr = factorial(n) // (factorial(r) * factorial(n-r))

# string formatting
result = "The binomial coefficient for {n} and {r} is {ncr}".format(n=n, r=r, ncr=ncr)
print(result)
