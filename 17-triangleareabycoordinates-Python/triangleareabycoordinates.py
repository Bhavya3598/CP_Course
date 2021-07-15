# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
import math
def distance(x1, y1, x2, y2):
	distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
	return distance
def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	a=distance(x1,y1,x2,y2)
	b=distance(x1,y1,x3,y3)
	c=distance(x2,y2,x3,y3)
	s=(a+b+c)/2
	A= math.sqrt(s*(s-a)*(s-b)*(s-c))
	x = round(A, 2)
	return A


	
print(triangleareabycoordinates(23, 30, 15, 15, 50, 25))