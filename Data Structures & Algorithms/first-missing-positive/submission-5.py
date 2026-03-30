class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 1
        for i in range(1,len(nums)+1):
            if res not in numSet:
                return res
            res += 1
            
        return res