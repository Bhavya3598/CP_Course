# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

summ=0
count=0
def fun_recursions_alternatingsum(l): 
	global summ
	global count
	if(len(l)==0):
		return 0
	elif(count%2==0):
		count+=1
		summ+=l[0]
		l.remove(l[0])
		fun_recursions_alternatingsum(l)
	else:
		count+=1
		summ-=l[0]
		l.remove(l[0])
		fun_recursions_alternatingsum(l)
	return summ



# def fun_recursions_alternatingsum(l): 
#     # your code goes here
#     if(len(l)==0):
#         return 0
#     else:
#         return l[0]-fun_recursions_alternatingsum(l[1:])


# print(fun_recursions_alternatingsum([81,23,90,134]))	

# ([5,3,8,4], 6), ([], 0), ([1,2,3,4], -2),
# ([99,56,23,98,45], 13), ([12,18,16,34,56], 32),
# ([81,23,90,134], 14)
# ])