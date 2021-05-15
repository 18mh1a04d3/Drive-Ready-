T=int(input())
a=0
b=7
for i in range(T):
    n=int(input())
    if (abs(a-n)<abs(b-n)):
        print("A")
        a=n
    elif(abs(a-n)>abs(b-n)):
        print("B")
        b=n
    else:
        if(a<b):
            print("A")
            a=n
        else:
            print("B")
            b=n
