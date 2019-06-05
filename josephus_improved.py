# The effective time complexity of the
# improved version is O(logN). For the
# problem statement, refer `josephus.py`

def josephus_v2(people, step=2):
  if step<=1:
    print("Enter step value, greater than 1")
  else:
    # len() method has O(1) time
    N = len(people) #caching the size of array
    p = 1
    # the loop runs for O(floor(logN)) time
    while p*2 < N:
      p = p*2
    # If N is a power of 2, should return 1. So let's check if L (N-p) is < p
    if N-p >= p:
      print(1)
    else:
      print((2*(N-p))+1)
    
num = int(input("Enter the number of soldiers: "))
soldiers = [i for i in range(1, num+1)] # generates a list of 1..num
josephus_v2(soldiers)
