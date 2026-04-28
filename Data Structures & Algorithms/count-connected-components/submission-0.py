class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        visit = set()
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)


        for i in range(n):
            if i not in visit:
                dfs(i)
                components += 1

        return components

        