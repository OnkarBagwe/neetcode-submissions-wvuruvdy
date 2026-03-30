class Solution:
    def validPalindrome(self, s: str) -> bool:
        # l = 0
        # r = len(s) - 1

        # while l < r:
        #     if s[l] != s[r]:
        #         skipL = s[l+1:r+1]
        #         skipR = s[l:r]
        #         return (skipL == skipL[::-1] or skipR == skipR[::-1])
        #     l += 1
        #     r -= 1
        # return True

        #space optimal
        l = 0
        r = len(s) - 1

        def isPali(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while l < r:
            if s[l] != s[r]:
                return(isPali(l+1,r) or isPali(l,r-1))
            l += 1
            r -= 1
        
        return True