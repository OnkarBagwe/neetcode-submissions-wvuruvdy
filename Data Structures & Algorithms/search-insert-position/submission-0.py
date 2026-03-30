class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        res = len(nums)
        while l <= r:
            m = l + (r-l)//2
            if nums[m] > target:
                res = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m
        
        return res