class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        tempSum = 0
        l, r = 0, 0

        while r < len(nums):
            tempSum += nums[r]
            while tempSum >= target:
                res = min(r-l+1,res)
                tempSum -= nums[l]
                l += 1
            r += 1
        return 0 if res == float("inf") else res