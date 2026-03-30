from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #approch 1
        # Time Complexity: O(n)
        # Spacr Complexity: O(n)
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

        #approach 2:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)