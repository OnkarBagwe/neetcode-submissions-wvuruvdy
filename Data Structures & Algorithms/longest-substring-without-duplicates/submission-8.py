class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #approach 1:
        res = set()
        l = 0
        resLen = 0

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1
            res.add(s[r])
            resLen = max(resLen, len(res))

        return resLen

        #approach 2:
        # hashmap = {}
        # res = 0
        # l = 0

        # for r in range(len(s)):
        #     if s[r] in hashmap:
        #         l = max(hashmap[s[r]] + 1, l)
        #     hashmap[s[r]] = r
        #     res = max(res, r - l + 1)
        # return res