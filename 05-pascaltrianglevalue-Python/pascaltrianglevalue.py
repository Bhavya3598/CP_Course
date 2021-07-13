# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




import math
def fun_pascaltrianglevalue(row, col):
  basic=row-col
  # flag=False
  if(basic>=0):
    basic=math.factorial(basic)
    a=math.factorial(row)
    b=math.factorial(col)
    c=b*(basic)
    result=a//c
    return result
  else:
    # flag=True
    return 0