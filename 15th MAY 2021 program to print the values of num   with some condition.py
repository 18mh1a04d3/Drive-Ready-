#program to print the values of num  if it is even divide it by 2 or if it is odd 3*n+1 upto 1 "
"""
let us take 6
6 is even so 6//2=3
3is odd so 3*3+1=10
10 is even so10//2=5
5 is odd so 3*5+1=16
16 is even so16//2=8
8 is even so8//2=4
4 is even so4//2=2
2is even so2//2=1
now stop procss when it reaches 1
so output is 6 3 10 5 16 8 4 2 1





"""
n=int(input())
k=n
print(k)
while n!=1:
    if(n%2==0):
        n=n//2
    elif(n%2!=0):
        n=3*n+1
    print(n)
