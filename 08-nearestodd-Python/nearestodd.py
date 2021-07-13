# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



import math
def fun_nearestodd(n):
	temp=int(n)
	if(temp%2==0):
		get_round=math.ceil(n)
		# print(get_round)
		if(get_round==temp):
			# get_round=get_round+1
			get_round=get_round-1
		return get_round
	else:
		return temp




