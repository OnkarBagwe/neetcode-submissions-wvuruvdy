class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # candidates.sort()
        # def dfs(i, curr, total):
        #     if total == target:
        #         res.append(curr.copy())
        #         return

        #     if i == len(candidates) or total > target:
        #         return

        #     curr.append(candidates[i])
        #     dfs(i+1, curr, total + candidates[i])
        #     curr.pop()

        #     while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
        #         i += 1
        #     dfs(i+1, curr, total)

        # dfs(0,[],0)

        # return res

        #optimal:
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res