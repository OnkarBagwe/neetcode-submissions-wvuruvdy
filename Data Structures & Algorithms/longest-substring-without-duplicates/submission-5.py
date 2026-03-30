class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hashmap = {}
        l = 0
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(hashmap[s[r]]+1,l)
            hashmap[s[r]] = r
            res = max(res, r-l+1)
        return res