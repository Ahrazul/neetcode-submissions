class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        visit, cycle = set(), set()
        res = []

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False

            if not preMap[crs]:
                res.append(crs)
            
            cycle.add(crs)

            for i in preMap[crs]:
                if not dfs(i):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            preMap[crs] = []
            res.append(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return res