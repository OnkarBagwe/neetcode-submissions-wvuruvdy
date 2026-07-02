from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #approach 1
        #Time complexity: O(n)
        #Space complexity: O(n)
        # hashmap = defaultdict(int)

        # for n in nums:
        #     if n in hashmap:
        #         return True
        #     hashmap[n] += 1

        # return False

        #approach 2
        #Time complexity: O(nlogn)
        #Space complexity: O(1) or O(n) depending on the sorting algorithm's implementation
        # nums = sorted(nums)
        # n = len(nums)

        # if n == 1:
        #     return False
        # for i in range(0, len(nums)):
        #     if nums[i] == nums [i-1]:
        #         return True
        # return False

        #approach 3:
        duplicate = set()

        for n in nums:
            if n in duplicate:
                return True
            duplicate.add(n)
        return False
