# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.

def fun_getaverage(s): 
	count=0
	lis=[]
	x=s.split(",")
	for i in x:
		try:
			if(i):
				# print(i)
				conv=int(i)
				lis.append(conv)
				# print(lis)
		except ValueError:
			continue
	length=len(lis)
	if(length==0):
		return 0.0
	else:
		add=sum(lis)
		output=(add/length)
		return output

	

	

print(fun_getaverage(("a,12,c,14,6,0")))

# ("13,excused,14,absent", 13.5), ("a,b,c",0.0),
# ("a,12,c,14,6,0", 8.0), ("1,2,3,4,5,6,7,8,9,10", 5.5),
# ("2,3,ddd4ff,34,1", 10.0)
# ])