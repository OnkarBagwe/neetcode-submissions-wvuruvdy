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

        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res