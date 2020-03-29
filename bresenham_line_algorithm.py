def lineGenerator(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1

	slope = 2*dy - dx

	x = x1
	y = y1
	while x < x2:

		#Print current coordinates
		print(x, y)

		#X increases any ways
		x+= 1

		# 2dy is always added in the slope. Do it.
		slope += 2*dy
		#Check for the current slope
		if slope >= 0:
			y += 1
			slope -= 2 * (x2-x1)

		elif slope <=0:
			#No changes are made.
			slope = slope


lineGenerator(3, 2, 15, 5)

	# if P1[0]==P2[0] and P1[1]==P2[1]:
	# 	return 0
	# #P1 is the point given. Initial point
	# #P2 is the point to reach. Final point
	# print(P1)
	# #Check if the point is above or below the line.
	# dx = P2[0]-P1[0]
	# dy = P2[1]-P1[0]

	# di = 2*dy - dx

	# currX = P1[0]
	# currY = P1[1]

	# if di > 0:
	# 	P1 = (currX+1, currY+1)
	# else:
	# 	P1 = (currX+1, currY)

	# return lineGenerator(P1, P2)