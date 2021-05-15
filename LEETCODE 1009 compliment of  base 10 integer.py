class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N==0:
            return 1
        c=1
        rev= 0
        while N:
            r=N%2
            N=N//2
            if r==0:
                r=1
            else:
                r=0
            rev=rev+r*c
            c=c*10
        p=0
        num=0
        while rev:
            r=rev%10
            rev=rev//10
            num=num+r*pow(2,p)
            p+=1
        return num
            
       
        
