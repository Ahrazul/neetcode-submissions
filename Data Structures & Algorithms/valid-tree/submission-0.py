class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        visit = set()

        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)

            for i in adj[node]:
                if i == prev:
                    continue
                if not dfs(i,node):
                    return False
            
            return True

            
        return dfs(0,-1) and n == len(visit)


            
        