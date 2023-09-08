
"""
Unit-1:
challenge-I

Factorial numbers
1!=1
2!=2*1
3!=3*2*1
...
...
...
10!=10*9*8*7*6*5*4*3*2*1
"""

def fact_rec(n):
 if n==0 or n==1 :
   return 1
 else:
   return n*fact_rec(n-1)
number=int(input("Enter a value :"))
rec=fact_rec(number)
print("The factorial number {} is {}.".format(number,rec))
