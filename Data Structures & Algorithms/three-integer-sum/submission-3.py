class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i,a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            l = i + 1
            r = n - 1

            while l < r:
                threeSum = nums[l] + nums[r] + a

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[l],nums[r],a])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res