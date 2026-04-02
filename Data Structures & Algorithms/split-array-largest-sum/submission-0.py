class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        res = r

        def canSplit(largest):
            subarray = 1
            curSum = 0

            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    curSum = n
            return True

        while l <= r:
            mid = l + (r-l)//2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res