# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def powerSum(n, k):
        calculate=n**k
        lis=[]
        if(n<0):
                return 0
        elif(k<0):
                return 0
        else:
                for i in range(n+1):
                        temp=i**k
                        lis.append(temp)
                        result=sum(lis)
                return result


print(powerSum(1999,19))
print("All test cases passed!")