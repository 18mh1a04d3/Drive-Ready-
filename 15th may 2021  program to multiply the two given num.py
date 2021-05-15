#program to multiply the two given num#
"""
let
a            b               s(it will takeb value  only when a value is odd)
13           24 ----->       24
13//2=6      24*2=48-        
6//2=3       48*2=96->       96
3//2=1       96*2=196->      192
                           --------
                             312
                           ----------
"""
n,m=map(int,input().split())#13 24
s=0
while n:
    if(n%2==1):#13%2==1
        s=s+m#0+24=24
    m=m*2#24*2=96
    n=n//2#13//2=6
print(s)
