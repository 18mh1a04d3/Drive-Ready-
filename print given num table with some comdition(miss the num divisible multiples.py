#if it is 5 table we haw to miss 5,10,15,20,....
n=int(input())
m=int(input())
for i in range(1,m+1):
    if n%2==0:
        continue
    print(n,"x",i,"=",n*i)
    

    
