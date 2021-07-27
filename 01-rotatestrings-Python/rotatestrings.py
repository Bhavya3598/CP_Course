# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, k):
	if(k>=0):
		for i in range(k):
			get_ele=s[0]
			new_s=s[1:]
			s=new_s+get_ele
		return s
	if(k<0):
		k=abs(k)
		for i in range(k):
			get_ele=s[-1]
			new_s=s[0:-1]
			s=get_ele+new_s
		return s

