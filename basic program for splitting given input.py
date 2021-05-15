#basic program for splitting given input
n=int(input())
while n:
    r=n%10     #it gives remainder
    n=n//10    #it gives quotient
    print(r,n)
