class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # n = len(envelopes)
        # envelopes.sort(key=lambda x: (x[0], -x[1]))

        # def lis(nums):
        #     LIS = [1]*n

        #     for i in range(n-1,-1,-1):
        #         for j in range(i+1,n):
        #             if nums[i] < nums[j]:
        #                 LIS[i] = max(LIS[i], 1 +LIS[j])

        #     return max(LIS)

        # return lis([e[1] for e in envelopes])

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            dp.append(nums[0])

            LIS = 1
            for i in range(1, len(nums)):
                if dp[-1] < nums[i]:
                    dp.append(nums[i])
                    LIS += 1
                    continue

                idx = bisect_left(dp, nums[i])
                dp[idx] = nums[i]

            return LIS

        return lis([e[1] for e in envelopes])