class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        state = [0] * numCourses #0 is unvisited, 1 is visiting, 2 is visited
        
        def dfs(node):
            if state[node] == 2: return True
            if state[node] == 1: return False

            state[node] = 1

            for nei in preMap[node]:
                if not dfs(nei): return False

            state[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True