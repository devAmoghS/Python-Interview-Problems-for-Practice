# Problem: A majority element in an array A[] of
# size n is an element that appears more than n/2
# times. Find the majority element in the given array.

# Returns the elements whose frequency is more than n/2
def findMajorityElement(elements, N, found=False):
    keys = [int(i) for i in elements.keys()]
    for i in keys:
        if elements[i] > N // 2:
            found = True
            print(i)
    if not found:
        print("Majority element not found")


# Creates a hash of frequency of numbers
def mapFrequency(arr):
    FREQUENCY = {}
    for i in arr:
        if i in FREQUENCY.keys():
            FREQUENCY[i] += 1
        else:
            FREQUENCY[i] = 0
    return findMajorityElement(FREQUENCY, len(arr))


arr = [1, 2, 4, 4, 4, 4, 4]
mapFrequency(arr)
