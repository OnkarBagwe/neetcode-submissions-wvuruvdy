class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}

        for pre,crs in prerequisites:
            adj[crs].append(pre)

        ans = []

        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()
                for pre in adj[crs]:
                    preMap[crs] |= dfs(pre)
                preMap[crs].add(crs)
            return preMap[crs]

        preMap = {}
        for crs in range(numCourses):
            dfs(crs)
        

        for u,v in queries:
            ans.append(u in preMap[v])

        return ans