# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math
def primenumber(n):
	if(n<1):
		return False
	for i in range(2, int(math.sqrt(n))+1):
		if (n%i==0):
			return False
	return True

def nthpowerfulnumber(n):
	count=0
	i=1
	if(n==0):
		return 1
	while(True):
		if(primefactor(i)):
			count+=1
		if(count==n+1):
			return i
		i=i+1
def primefactor(n):
	lis=[]
	count=0
	if(n<1):
		return False
	for i in range(1,n+1):
		# print(i)
		if(n%i==0):
			# print(i)
			if(primenumber(i)):
				# print('yes')
				lis.append(i)
				if(n%(i**2)==0):
					count+=1
	if count==len(lis) and (count!=0 and lis!=0 ):
			return 	True
	else:
		return False

# (53, 972), 
# 	(39, 576), 
# 	(29, 343), 
# 	(17, 128), 
# 	(18, 144), 
# 	(19, 169), 
# 	(4, 16), 
# 	(5, 25), 
# 	(6, 27), 
# 	(7, 32), 
# 	(8, 36), 
# 	(9, 49), 
# 	(10, 64), 
# 	(0, 1)

# print(primefactor(1000))
# print(primenumber(23))
# print(nthPowerfulNumber(39))
