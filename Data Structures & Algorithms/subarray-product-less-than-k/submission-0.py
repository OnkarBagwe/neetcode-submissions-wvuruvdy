class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        prefix = 1
        res = 0
        for r in range(len(nums)):
            prefix *= nums[r]
            while l <= r and prefix >= k:
                prefix //= nums[l]
                l += 1
            res += (r-l+1)
        return res