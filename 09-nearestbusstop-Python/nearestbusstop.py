# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	lis=[]
	if(street==0):
		return 0
	elif(street>0):
		for i in range(0,street,8):
			lis.append(i)
			last=lis[-1]
			diff=street-last
		if(diff<=4):
			return last
		elif(diff>=5):
			return last+8
		elif(diff==0):
			return street
print(fun_nearestbusstop(4))

# (12, 8), (8, 8),
#     (13, 16), (0, 0),
#     (5, 8), (16, 16),
#     (4, 0)