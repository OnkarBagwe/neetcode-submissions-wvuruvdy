class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #DP (Top-Down)

        # dp = {}

        # def dfs(i,total):
        #     if i == len(nums):
        #         return 1 if total == target else 0

        #     if (i,total) in dp:
        #         return dp[(i,total)]

        #     dp[(i,total)] = (dfs(i+1, total+nums[i]) + 
        #                      dfs(i+1, total-nums[i]))
        #     return dp[(i,total)]

        # return dfs(0,0)

        #DP (Botttom-Up)

        # n = len(nums)
        # dp = [defaultdict(int) for _ in range(n+1)]
        # dp[0][0] = 1

        # for i in range(n):
        #     for total,count in dp[i].items():
        #         dp[i+1][total+nums[i]] += count
        #         dp[i+1][total-nums[i]] += count
        # return dp[n][target]

        #DP (Botttom-Up) Space optimize

        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(n):
            next_dp = defaultdict(int)
            for total,count in dp.items():
                next_dp[total+nums[i]] += count
                next_dp[total-nums[i]] += count
            dp = next_dp
        return dp[target]