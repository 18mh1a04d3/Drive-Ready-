class Solution:
    def totalMoney(self, n: int) -> int:
        d=0
        s=0
        c=0
        w=0
        while(d<n):
            d+=1
            c+=1
            s=s+c
            if(d%7==0):
            
                c=w+1
                w+=1
        return s
        
