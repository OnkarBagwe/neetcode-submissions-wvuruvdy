class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums + nums
        # return ans

        # n = len(nums)
        # ans = [0] * (2 * n)
        # for i, num in enumerate(nums):
        #     ans[i] = ans[i + n] = num
        # return ans

        n = len(nums)
        ans = [0] * (n*2)
        for i in range(n):
            ans[i] = ans[i+n] = nums[i]
        return ans