class Solution:
    def __init__(self):
        self.res = 0

    def countSubstrings(self, s: str) -> int: 
        for i in range(len(s)):
            self.res += self.countPali(s,i,i)
            self.res += self.countPali(s,i,i+1)
        
        return self.res
    
    def countPali(self,s,l,r):
        self.res = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            self.res += 1
            l -= 1
            r += 1
        return self.res