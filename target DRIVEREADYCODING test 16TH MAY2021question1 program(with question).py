#Sandhya, a software analyst bought a new split-Ac to her house. She was researching her Ac’s temperature limits by increasing and decreasing. The table is as follows#
"""
sample Input

Sample Output

>=16 and<=25

very cool

>25 and <=32

cool

>32

no effect

                 

 
 
Sample input1:
17
Sample Output1:
very cool
Sample Input 2:
35
Sample Output:
no effect
"""


#program#


n=int(input())
if(n>=16 and n<=25):
    print("very cool")
elif(n>25 and n<=32):
    print("cool")
else:
    print("no effect")
