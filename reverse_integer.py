"""
Problem No: 07
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321
    Example 3:

Example 3:
    Input: x = 120
    Output: 21
"""

class Solution(object):
    def reverse(self, x):
        if x == 0:
           return 0
         
        negative = True if x < 0 else False
        num = str(abs(x))
        num_len = len(num)

        if num[-1] == "0":
           num = num[:num_len - 1]

        result = 0 - int(num[::-1]) if negative == True else int(num[::-1])
        if abs(result) > 2**31-1 :
           return 0
        else:
          return result




        

s = Solution()
for i in [-123,9646324351,140, 320, 331]:
  print(s.reverse(i))
        