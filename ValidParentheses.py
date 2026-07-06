"""
Valid Parentheses:

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""

class Solution(object):
    brackets = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    def isValid(self, s):
        stack = []
        if len(s) == 1:
            return False
        if s[0] not in self.brackets:
            return False
        for char in s:
            if char in self.brackets:
                stack.append(self.brackets[char])
                print(char, self.brackets[char])
            else:
                if len(stack) == 0:
                    return False
                if char == stack[-1]:
                    stack.pop()
                if char != stack[-1]:
                    return False
        return len(stack) == 0

sol = Solution()
print(sol.isValid("(])"))