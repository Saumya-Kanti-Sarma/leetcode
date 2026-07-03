'''
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''

class Solution(object):
    def isPalindrome(self, x):
        strX = str(x)
        revStrX = strX[::-1]
        if strX[0] == "-":
            return False
        elif int(revStrX) == x:
            return True
        else:
            return False
'''
This was simple question that I have solved in my sem 1 python practical. 
I've hardcoded to return False for all -ve numbers as no negative number will have palindrome.
03/07/2026
'''