# program to count no of digits in given input
n=int(input())
c=0
while n:
    r=n%10     #it gives remainder
    n=n//10    #it gives quotient
    c=c+1
print(c)
