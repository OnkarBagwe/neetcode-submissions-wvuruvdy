class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        prefixSum = {0:1}

        res = 0

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res