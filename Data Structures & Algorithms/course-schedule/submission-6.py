class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)

        for crs,pre in prerequisites:
            prereq[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if prereq[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            prereq[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True