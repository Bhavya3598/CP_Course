# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    count=0
    lis=[]
    a=s1.upper()
    b=s2.upper()
    # c=list(map(str,a))
    # d=list(map(str,b))
    if(len(a)==len(b)):
        for i in range(len(b)):
            p=a.count(a[i])
            q=b.count(a[i])
            if(p==q):
                return True
            return False
    return False
# print(areAnagrams('aba', 'abc'))