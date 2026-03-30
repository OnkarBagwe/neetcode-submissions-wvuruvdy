from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #approach 1
        hashmap = defaultdict(int)

        for n in nums:
            if n in hashmap:
                return True
            hashmap[n] += 1

        return False