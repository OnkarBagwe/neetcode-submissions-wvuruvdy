from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #approach 1
        # hashmap = defaultdict(int)

        # for n in nums:
        #     if n in hashmap:
        #         return True
        #     hashmap[n] += 1

        # return False

        #approach 2

        nums = sorted(nums)
        n = len(nums)

        if n == 1:
            return False
        for i in range(0, len(nums)):
            if nums[i] == nums [i-1]:
                return True
        return False
