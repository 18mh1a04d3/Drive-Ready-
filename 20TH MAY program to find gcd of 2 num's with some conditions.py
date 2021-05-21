# 20TH MAY program to find gcd of 2 num's with some conditions#
"""
12 38   a must be less than b then 
12 38%12=2
12 2       so swap as a>b
2 12
2 12%2=0
2 0    when b becomes 0 then a is the gcd
"""


def gcd(a,b):

    while True:
        if a>b:
            
            
            temp=a
            a=b
            b=temp
        b=b%a
        if b==0:
            return a
a,b=map(int,input().split())
print(gcd(a,b))
