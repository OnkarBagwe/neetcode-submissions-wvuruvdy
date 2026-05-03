class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = max(nums)
        # curMin, curMax = 1,1

        # for n in nums:
        #     tmp = curMax * n
        #     curMax = max(tmp, curMin * n, n)
        #     curMin = min(tmp, curMin * n, n)
        #     res = max(res,curMax)

        # return res

        #2:

        res = nums[0]
        prefix = 0
        suffix = 0
        n = len(nums)

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n-i-1] * (suffix or 1)
            res = max(res, max(prefix,suffix))

        return res