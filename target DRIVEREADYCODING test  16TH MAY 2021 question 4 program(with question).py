#Difference between sums of odd and even digits
Given a long integer, we need to find if the difference between sum of odd position digits and sum of even position digits is 0 or not. The indexes start from zero (0 index is for leftmost digit).#
"""

Examples:

Input : 1212112
Output : Yes
Explanation:-
the odd position element is 2+2+1=5
the even position element is 1+1+1+2=5
the difference is 5-5=0.so print yes.

Input :12345
Output : No
Explanation:-
the odd position element is 1+3+5=9
the even position element is 2+4=6
the difference is 9-6=3 not  equal
to zero. So print no.
For example:

Test	Input	Result
1
1212112
yes
"""
#PROGRAM#
n=int(input())
x=0
y=1
while n:
    y=y+1
    r=n%10
    n=n//10
    if y%2==1:
        x=x+r
if x%2==1:
    print("yes")
elif x%2==0:
    print("no")
