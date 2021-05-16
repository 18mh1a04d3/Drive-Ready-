#find out whether given number is palindrome or not

 palindrome: if given number and its reversed number are the same then its a palindrome#
"""
Sample Input1:

234

sample Ouput1:

not palindrome

Sample Input2:

121

sample Ouput2:

palindrome






For example:

Test	Input	     Result
1       234       not palindrome

"""

#PROGRAM#
n=int(input())
k=n
reverse=0
while(n>0):
    r=n%10
    reverse=reverse*10+r
    n=n//10
if(k==reverse):
    print("palindrome")
else:
    print("not palindrome")
