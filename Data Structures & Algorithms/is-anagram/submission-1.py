from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h1 = defaultdict(str)
        h2 =defaultdict(str)

        for l in s:
            if l in h1:
                h1[l] += 1
            else:
                h1[l] = 1

        for l in t:
            if l in h2:
                h2[l] += 1
            else:
                h2[l] = 1

        if h1 == h2:
            return True
        else:
            return False