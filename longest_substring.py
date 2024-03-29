'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring,without repeating characters.
'''
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)
        while(left < n and right < n):
            el = s[right]
            if(el in m):
                left = max(left, m[el]+1)
            m[el] = right

            ans = max(ans,right-left+1)
            right+=1

        return ans

s = Solution()
s.lengthOfLongestSubstring()
