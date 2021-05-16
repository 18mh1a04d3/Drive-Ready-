# Jhon and Mr Javid are best friends, and javid is habbituated to read in right to left, write a logic to take a number in jhon point of view and print it in Javid perspective#

"""

i/p:

1234

o/p:

4321



For example:

Test	Input	Result
1       2431    1342


2      97389    98379
"""


#PROGRAM#
n=int(input())
k=n
rev=0
while (n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
