# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	negativee=False
	con_str=str(n)
	if(n<0):	
		con_str=str((abs(n)))
		negativee=True
	my_lis=list(map(str,con_str))
	my_lis.reverse()
	redu=len(my_lis)-1
	if(k<=redu):
		my_lis.pop(k)
		my_lis.insert(k, d)
		my_lis.reverse()
		a=list(map(str,my_lis))
		result="".join(a)
		result=int(result)
		if(negativee==True):
			return -(result)
		else:
			return result
	else:
		my_lis.insert(k, d)
		my_lis.reverse()
		a=list(map(str,my_lis))
		result="".join(a)
		result=int(result)
		if(negativee==True):
			return -(result)
		else:
			return result