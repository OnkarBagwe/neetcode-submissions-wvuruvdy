class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])

            cur.pop()
            dfs(i+1, cur, total)

        dfs(0,[],0)

        return res


        #optimize:
        # res = []
        # nums.sort()

        # def dfs(i,curr,total):
        #     if total == target:
        #         res.append(curr.copy())
        #         return
            
        #     for j in range(i,len(nums)):
        #         if total + nums[j] > target:
        #             return
        #         curr.append(nums[j])
        #         dfs(j,curr,total+nums[j])
        #         curr.pop()
        
        # dfs(0,[],0)
        # return res
