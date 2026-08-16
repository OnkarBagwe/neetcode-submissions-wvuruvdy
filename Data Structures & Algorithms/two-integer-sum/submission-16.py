class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #approach 1:
        # indices = {}

        # for i, n in enumerate(nums):
        #     indices[n] = i

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in indices and indices[diff] != i:
        #         return [i, indices[diff]]
        # return []

        #approach 2:
        indices = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indices:
                return [indices[diff],i]
            indices[nums[i]] = i