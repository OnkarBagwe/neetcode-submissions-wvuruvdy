class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for n in nums:
            if n == 0:
                res = max(res, cnt)
                cnt = 0
            else:
                cnt += 1
        
        return res