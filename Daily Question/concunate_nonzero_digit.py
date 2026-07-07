"""
Question no: 3754.
Concatenate Non-Zero Digits and Multiply by Sum I
(Easy)

You are given an integer n.
Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0. 
Let sum be the sum of digits in x.

Return an integer representing the value of x * sum.

Example 1:
    Input: n = 10203004
    Output: 12340
    Explanation:
      The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
      The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
      Therefore, the answer is x * sum = 1234 * 10 = 12340.

Example 2:
    Input: n = 1000
    Output: 1
    Explanation:
      The non-zero digit is 1, so x = 1 and sum = 1.
      Therefore, the answer is x * sum = 1 * 1 = 1.
"""

class Solution(object):
    def sumAndMultiply(self, n):
        n = list(str(n))
        ns = []
        sum = 0
        for i in n:
            if i != "0":
                ns.append(i)
            sum += int(i)
        
        if not ns:  #len(ns) == 0
            return 0          
        num = int("".join(ns))
        return num * sum
    
soln = Solution()
print(soln.sumAndMultiply(10203004))