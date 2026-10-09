class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        # if sum(nums) % k != 0:
        #     return False

        # nums.sort(reverse=True)
        # target = sum(nums) // k
        # used = [False] * len(nums)

        # def backtrack(i, k, subsetSum):
        #     if k == 0:
        #         return True
        #     if subsetSum == target:
        #         return backtrack(0, k - 1, 0)
        #     for j in range(i, len(nums)):
        #         if used[j] or subsetSum + nums[j] > target:
        #             continue
        #         used[j] = True
        #         if backtrack(j + 1, k, subsetSum + nums[j]):
        #             return True
        #         used[j] = False
        #     return False

        # return backtrack(0, k, 0)

        #Backtracking + memoization: O(N*2^N)
        n = len(arr)
    
        total_array_sum = sum(arr)
        
        # If the total sum is not divisible by k, we can't make subsets.
        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        taken = ['0'] * n
        
        memo = {}
        
        def backtrack(index, count, curr_sum):
            n = len(arr)
            
            taken_str = ''.join(taken)
      
            # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True
            
            # No need to proceed further.
            if curr_sum > target_sum:
                return False
            
            # If we have already computed the current combination.
            if taken_str in memo:
                return memo[taken_str]
            
            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                memo[taken_str] = backtrack(0, count + 1, 0)
                return memo[taken_str]
            
            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if taken[j] == '0':
                    # Include this element in current subset.
                    taken[j] = '1'
                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True
                    # Backtrack step.
                    taken[j] = '0'
                    
            # We were not able to make a valid combination after picking 
            # each element from the array, hence we can't make k subsets.
            memo[taken_str] = False
            return memo[taken_str] 
        
        return backtrack(0, 0, 0)