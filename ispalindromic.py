# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.
# assert (isPalindromicPrime(2) == True)
# assert (isPalindromicPrime(10) == False)
# assert (isPalindromicPrime(104) == False)
# assert (isPalindromicPrime(235) == False)
# assert (isPalindromicPrime(131) == True)
# assert (isPalindromicPrime(900) == False)
# assert (isPalindromicPrime(101) == True)
# assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
# assert (isPalindromicPrime(121) == False)
import math
def isPalindromicPrime(n):
	lis=[]
	if(primenumber(n)):
		lis.append(n)
		# print(lis)
		rev=lis[::-1]
		org=lis
		if(org==rev):
			return True
	return False

def primenumber(n):
	if(n<1):
		return False
	else:
		for i in range(2,(math.isqrt(n))+1):
			# print(i)
			if(n%i==0):
				return False
		return True
# print(primenumber(131))
print(isPalindromicPrime(2))


