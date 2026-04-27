class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def countSort(nums):
            count = defaultdict(int)
            maxN, minN = max(nums), min(nums)
            for n in nums:
                count[n] += 1
            
            i = 0
            for n in range(minN, maxN + 1):
                while count[n] > 0:
                    nums[i] = n
                    i += 1
                    count[n] -= 1
            return nums

        return countSort(nums) 