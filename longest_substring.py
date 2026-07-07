"""
Question No: 03 (easy)

Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s = list(s) # [a,b,c,a,b,c,b,b]
        longest = ""
        word = []
        while len(s) != 0:
            for char in s:
                if char not in word:
                    word.append(char)
                else:
                    w = "".join(word)
                    if len(longest) < len(w):
                        longest = w
                    word = []
                    if len(s) != 0:
                        s.pop(0)   
                        break
                    else:
                        break
        
        return len(longest)