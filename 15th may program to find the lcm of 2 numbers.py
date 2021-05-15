#program to print the lcm of 2 nums with some conditions#
"""
let us take
           2 |12 24       2 nos should be exactly divisble
           -----------    
           2 |6  12          
           -----------
           3 |3  6          here 2 is not exactly divisible so  +1 increment
           -----------      if any one num is less than the divisor end the process
           3|1   2           noe multiply all like   1*2*3*2*2=24

        




""""
a,b=map(int,input().split())
x=2
c=1
while True :
    if(a%x==0 and b%x==0):
        a=a//x
        b=b//x
        c=c*x
    elif x>=a or x>=b:
        c=c*a*b
        break
    else:
        x=x+1
print(c)
