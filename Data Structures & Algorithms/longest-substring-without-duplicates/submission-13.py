class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        longest = 0
        while r <len(s):
            while s[r] in s[l:r]:
                l+=1
            r+=1
            longest = max(longest, r-l)
        return longest