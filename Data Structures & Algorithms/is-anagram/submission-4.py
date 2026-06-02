from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #approch 1
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # h1 = defaultdict(str)
        # h2 =defaultdict(str)

        # for l in s:
        #     if l in h1:
        #         h1[l] += 1
        #     else:
        #         h1[l] = 1

        # for l in t:
        #     if l in h2:
        #         h2[l] += 1
        #     else:
        #         h2[l] = 1

        # if h1 == h2:
        #     return True
        # else:
        #     return False

        # Time Complexity: O(nlogn)
        # Space Complexity: O(1)
        #approach 2:
        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)

        #approach 3:
        # countS = [0]*26
        # countT = [0]*26
        # if len(s) != len(t):
        #     return False
        # for i in range(len(s)):
        #     countS[ord(s[i]) - ord('a')] += 1
        #     countT[ord(t[i]) - ord('a')] += 1
    
        # if countS == countT:
        #     return True
        # else:
        #     return False

        #approach 4:
        l1 = len(s)
        l2 = len(t)
        if l2 != l1:
            return False
        
        count = [0] * 26
        for i in range(l1):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        for c in count:
            if c != 0:
                return False
        
        return True