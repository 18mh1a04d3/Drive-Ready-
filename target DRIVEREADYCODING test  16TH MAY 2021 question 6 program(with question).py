#write a program that adds two numbers prints the sum to STDOUT  . read the input from STDIN. the first line of your input will contain an integer (N) that tells you how many more lines there are in the input each of the subsequent N lines contains 2 integers. you need to print the sum of each pair on a separate line of STDOUT.#
"""
sample input

3
1   5
3   10 
999   -34343

Sample Output:

6
13
-33344

For example:

Test	Input	         Result
1           3 
         1    5               6
         3   10              13

        999 -34343        -33344


"""
#PROGRAM#
n=int(input())
for _ in range(n):
    l,r=map(int,input().split())
    print(l+r)
