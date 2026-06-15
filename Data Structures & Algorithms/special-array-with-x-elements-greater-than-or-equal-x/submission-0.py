class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)

        for n in nums:
            idx = min(n, len(nums))
            count[idx] += 1

        total_right = 0

        for i in range(len(nums), -1, -1):
            total_right += count[i]
            if i == total_right:
                return total_right

        return -1