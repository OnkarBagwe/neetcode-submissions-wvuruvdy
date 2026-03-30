class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        # for i,n in enumerate(nums):
        #     indices[n] = i

        for i,n in enumerate(nums):
            diff = target - n
            if diff in indices:
                return [indices[diff], i]
            else:
                indices[n] = i

        return []