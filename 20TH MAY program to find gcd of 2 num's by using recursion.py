#20TH MAY program to find gcd of 2 num's by using recursion#



"""

*** for using functions both fun call and fun def should be there***
fun call ----  function should be there and then it performs operation
fun def  ----  define
pass means nothing is there like an empty
for defining function def is declared
syntax:def name
functions are 2 types we use:
1.with return value(if func call is assigned with variable or it is assigned in print or it given in any statment condition)
2.without return value(
recursion means calling itself



"""
def gcd(a,b):
    if b==0:
        return a
    if a>b:
        a,b=b,a
    return  gcd(a,b%a)
        
    

  
        
            
a,b=map(int,input().split())
print(gcd(a,b))





#another condition program for gcd using recusion#
def gcd(a,b):
    if b==0:
        return a
    if a>b:
        a,b=b,a
    return  1+gcd(a,b%a)
        
    

  
        
            
a,b=map(int,input().split())
print(gcd(a,b))









