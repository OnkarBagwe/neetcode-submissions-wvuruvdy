class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 != 0:
            return False
        
        target = s//2

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            nxtDP = dp.copy()
            for t in dp:
                if t+nums[i] == target:
                    return True
                nxtDP.add(t+nums[i])
            dp = nxtDP
        return True if target in dp else False