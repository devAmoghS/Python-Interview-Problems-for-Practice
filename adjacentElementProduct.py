# Given an array of integers, find the pair of adjacent elements 
# that has the largest product and return that product.

# Approach 1: (Brute Force) - Check all the pairs in the list and then return the maximum pair
# Time Complexity: O(N^2)

def adjacentElementProductBF(inputArray):
	largestProduct = -999999
	
	# for sanity check, assert if array contains at least 2 elements
	if len(inputArray) < 2:
		print("No pairs exists")
		return -1
	
	for i in range(0, len(inputArray)):
		for j in range(i+1, len(inputArray)):
			currentProduct = inputArray[i]*inputArray[j]
			
			if currentProduct > largestProduct:
				largestProduct = currentProduct
	
	return largestProduct

# Approach 2: (Sort & Pick Last Pair) - Sort the list and then pick the last two numbers
# Caveat: All elements must be positive
# Time Complexity: O(Nlog(N))

def adjacentElementsProductSort(inputArray):
	size = len(inputArray)
	
	if size < 2:
		print("No Pairs exist")
		return -1
	
	sortedArray = sorted(inputArray)
	return sortedArray[-1] * sortedArray[-2] 


def adjacentElementsProduct(inputArray):	

	length = int(len(inputArray))

	maxm = inputArray[0]*inputArray[1]
	product = 1
	for i in range(1, length-1):
		product = inputArray[i]*inputArray[i+1]

		if product>maxm:
			maxm = product

	return maxm


# print(adjacentElementsProduct([3,6,7,5]))

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
    
#Alternate solution
#return max([inputArray[i]*inputArray[i+1] for i in range(0, int(len(inputArray)-1))])
