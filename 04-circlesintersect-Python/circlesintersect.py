# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.



import math
def distance(x1,x2,y1,y2):
	route=math.sqrt((x2-x1)**2+(y2-y1)**2)
	return route
	
def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	val=distance(x1,x2,y1,y2)
	if(val<=r1+r2):
		return True
	else:
		return False