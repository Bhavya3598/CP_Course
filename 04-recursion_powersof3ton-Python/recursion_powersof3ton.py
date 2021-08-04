# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def powersof3ton(n,lis,count,power):
	power=3**count
	if(power<=n):
		lis.append(power)
	count+=1
	if(power>=n):
		return lis
	return powersof3ton(n,lis,count,power)

def recursion_powersof3ton(n):
	# Your code goes here
	lis=[]
	if(n<1):
		return None
	else:
		return powersof3ton(n,lis,0,0)