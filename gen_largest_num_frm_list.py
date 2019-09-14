# Write a function that given a list of non 
# negative integers, arranges them such that 
# they form the largest possible number. For 
# example, given [50, 2, 1, 9], the largest 
# formed number is 95021

from itertools import permutations

def generate_largest_number(arr):
  gen_nums = []
  for i in permutations(arr, len(arr)):
    gen_nums.append("".join(map(str, i)))
  return max(gen_nums)

arr = [54, 546, 548, 60]
generate_largest_number(arr)
