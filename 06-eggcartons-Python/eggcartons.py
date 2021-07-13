# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	hold=12
	if(eggs==0):
		return 0
	elif(eggs<=12):
		return 1 
	elif(eggs>12):
		rem=eggs%12
		quo=eggs//12
		result=rem+quo
		return result
print(fun_eggcartons(0))