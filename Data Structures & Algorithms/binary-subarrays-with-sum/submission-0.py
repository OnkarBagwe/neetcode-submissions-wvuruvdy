class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #Count no. of subaarays where curSum <= x 
        def helper(x):
            if x < 0:
                return 0
            res = 0
            curSum = 0
            l = 0
            for r in range(len(nums)):
                curSum += nums[r]
                while curSum > x:
                    curSum -= nums[l]
                    l += 1
                res += r-l+1
            return res

        return helper(goal) - helper(goal-1)