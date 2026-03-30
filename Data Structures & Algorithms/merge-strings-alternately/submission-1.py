class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # w1 = len(word1)
        # w2 = len(word2)
        # i = 0
        # j = 0
        # res = ""
        # while i < w1 or j < w2:
        #     if i < w1:
        #         res += word1[i]
        #     if j < w2:
        #         res += word2[j]
        #     i += 1
        #     j += 1
        
        # return res
        
        n, m = len(word1), len(word2)
        res = []
        for i in range(max(m, n)):
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])
        return "".join(res)