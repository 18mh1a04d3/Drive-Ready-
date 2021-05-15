#program for splitting even and odd digits and forming a num with those digits from given integer#
n=int(input())
a=A=0
b=B=0
C=D=0
while n!=0:
    r=n%10
    n=n//10
    if(r%2==0):
        a=a+1
        A=A*10+r
    else:
        b=b+1
        B=B*10+r
while A:
    r=A%10
    A=A//10
    C=C*10+r
while B:
    r=B%10
    B=B//10
    D=D*10+r
print(C,D)
    
    
