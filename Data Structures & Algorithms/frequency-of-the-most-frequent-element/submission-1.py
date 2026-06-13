class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        l = 0
        r = 0
        n = len(nums)
        nums.sort()
        
        while r < n:
            total += nums[r]

            while nums[r] * (r-l+1) > total + k:
                total -= nums[l]
                l += 1

            res = max(res, r-l+1)
            r += 1

        return res