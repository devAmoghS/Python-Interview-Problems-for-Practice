# Bresenham Line Algorithm (BLA) is one of the earliest algorithms developed
# in computer graphics. It is used for drawing lines.  It is an efficient method because 
# it involves only integer addition, subtractions, and multiplication operations. 

# These operations can be performed very rapidly so lines can be generated quickly.

# Reference: http://floppsie.comp.glam.ac.uk/Southwales/gaius/gametools/6.html

# Algorithm:
# 1. We are given the starting and ending point (x1, y1) and (x2, y2)
# 2. We compute the gradient m, using the formula: m = (y2-y1)/(x2-x1)
# 3. The equation of the straight line is y = m*x+c. So the next thing we need to find is the intercept c
# 4. Intercept can be derived using the formula c = y1 - m*x1
# 5. To get the next point, we add dx to the x-cordinate and dy to the y cordinate
# 6. We continue this cycle until we reach (x2, y2)

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


# lineGenerator(3, 2, 15, 5)

# 	# P1 is the point given. Initial point
# 	# P2 is the point to reach. Final point
# 	if P1[0] == P2[0] and P1[1] == P2[1]:
# 		return 0
# 	print(P1)
# 	#Check if the point is above or below the line.
# 	dx = P2[0]-P1[0]
# 	dy = P2[1]-P1[0]

# 	di = 2*dy - dx

# 	currX = P1[0]
# 	currY = P1[1]

# 	if di > 0:
# 		P1 = (currX+1, currY+1)
# 	else:
# 		P1 = (currX+1, currY)

# 	return lineGenerator(P1, P2)
