# This method returns the sum of numbers
# present till each index

def getPrefixArray(arr):
  return [sum(arr[:i]) for i in range(1, len(arr)+1)]

# This method will create a mapping of numbers
# and the indices they are present at

def getIndexMap(arr):
  indexMap = {}

  for i in range(len(arr)):
    if arr[i] not in indexMap.keys():
      indexMap[arr[i]] = [i,]
    else:
      indexMap[arr[i]].append(i)
  
  return indexMap

# This method will create the sum prefix of the 
# current array, if the sum is repeating, then
# there is a zero sum sub array

def hasZeroSum(arr):
  prefixArr = getPrefixArray(arr)
  sumAtIndexMap = getIndexMap(prefixArr)

  for v in sumAtIndexMap.values():
    if len(v) > 1:
      return True
      break
  return False    


ipArray = [1, 4, -2, -2, 5, -4, 3]
hasZeroSumTrue = hasZeroSum(ipArray)
print(hasZeroSumTrue)
