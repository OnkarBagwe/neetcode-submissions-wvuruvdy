class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        cycle = set()
        def dfs(crs):
            if crs in visit:
                return False
            if crs in cycle:
                return False
            
            visit.add(crs)
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            cycle.remove(crs)
            return True

        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True