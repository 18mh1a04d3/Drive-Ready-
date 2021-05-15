#if we give input 5 20 it should print upto answer value 20
k,t=map(int,input().split())
for i in range(1,t+1):
    L=i*k
    print(k,"x",i,"=",L)
    if L==t:
          break
