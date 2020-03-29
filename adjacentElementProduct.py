#Given an array of integers,
#find the pair of adjacent elements 
#that has the largest product and 
#return that product.

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








