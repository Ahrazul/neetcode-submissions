class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1: return False
            if state[node] == 2: return True

            state[node] = 1

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            state[node] = 2
            res.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res