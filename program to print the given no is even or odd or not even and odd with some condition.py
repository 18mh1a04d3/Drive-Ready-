# program to print the given no is even or odd or not even and odd with some condition#
"""
in given integer if the
no of even digit count is even times then print even
no of odd digit count is odd times then print odd
else:
print not even and odd
"""
n=int(input())
e=0
o=0
while n>0:
    r=n%10
    n=n//10
    if r%2==0:
        e=e+1
    else:
        o=o+1
print(e)
print(o)
if(e%2==0):
    print("even")
if(o%2!=0):
    print("odd")
if(e%2!=0 and o%2==0):
    print("not even and odd")
