class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        # rob1 = 0
        # rob2 = 0

        # for n in nums:
        #     newRob = max(rob1+n, rob2)
        #     rob1 = rob2
        #     rob2 = newRob
        
        # return rob2
        n = len(nums)
        
        dp = [0]*n
        dp[0] = nums[0]

        for i in range(1,n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[-1]