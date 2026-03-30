class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        n = len(nums)
        postfix = 1
        res = [1] * n

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res