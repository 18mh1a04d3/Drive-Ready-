#7. Reverse Integer#

"""
Easy



Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""

#program#
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            s=-1
        else:
            s=1
        x=abs(x) 
        rev=0
        while (x>0):
            r=x%10
            rev=rev*10+r
            x=x//10
        rev=rev*s
        if (rev >= -2**31 and rev <= 2**31 - 1):
            return rev
        else: 
            return 0
        return rev
        
