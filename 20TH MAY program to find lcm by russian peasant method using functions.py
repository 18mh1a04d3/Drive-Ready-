#program to find lcm by russian peasant method using functions#
"""
let us take
           2 |12 24       2 nos should be exactly divisble
           -----------    
           2 |6  12          
           -----------
           3 |3  6          here 2 is not exactly divisible so  +1 increment
           -----------      if any one num is less than the divisor end the process
           3|1   2           noe multiply all like   1*2*3*2*2=24
        
"""
def lcm(a,b):
    t=2
    r=1
    while(a>=t and b>=t):
        if a%t==0 and b%t==0:
            a=a//t
            b=b//t
            r=r*t
        else:
            t+=1
        if a<t or b<t:
            return r*a*b
a,b=map(int,input().split())
print(lcm(a,b))
