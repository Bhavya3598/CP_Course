# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	count=0
	i=309
	if(n==0):
		return i
	while(True):
		if(withproperty309(i)):
			count+=1
		if(count==n+1):
			return i
		i=i+1

def withproperty309(n):
	a=n**5
	b=str(a)
	d=list(b)
	# print(d)
	if ('0' in d)and('1' in d)and('2' in d)and('3' in d)and('4' in d)and('5' in d)and('6' in d)and('7' in d)and('8' in d)and('9' in d):
		return True
	return False
print(nthwithproperty309(0))