class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        i = 0
        j = 0
        res = ""
        while i < w1 or j < w2:
            if i < w1:
                res += word1[i]
            if j < w2:
                res += word2[j]
            i += 1
            j += 1
        
        return res