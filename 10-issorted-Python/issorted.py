# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def sortedlis(a):
	lis2=[]
	copy=a
	while(a):
		min=a[0]
		for i in a:
			if(i<min):
				min=i
		lis2.append(min)
		a.remove(min)
	return lis2
def issorted(n):
	copy=[]
	to_rev=[]
	for i in n:
		copy.append(i)
		to_rev.append(i)
	rev=to_rev.reverse()
	org=sortedlis(n)
	if(org==copy):
		return True
	elif(org==to_rev):
		return True
	return False