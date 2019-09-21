def getMinPlatforms(arr, dep):
  if len(arr) != len(dep):
    print("Wrong inputs given...")
    return
  else:
    sorted_arr = sorted(arr + dep)
    
    minPlatform = 0
    trainsAtPlatform = 0

    for i in sorted_arr:
      if i in arr:
        trainsAtPlatform += 1
      if i in dep:
        trainsAtPlatform -= 1
      minPlatform = max(minPlatform, trainsAtPlatform)
    
    return minPlatform

arrivalArr = [900, 940, 950, 1100, 1500, 1800] 
departureArr = [910, 1200, 1120, 1130, 1900, 2000]

result = getMinPlatforms(arrivalArr, departureArr)

print("Minimum no. of platforms for given time table are: ", result)
