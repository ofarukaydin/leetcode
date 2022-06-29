#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        visited = set()

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            print('visited:' + ' ' + str(node))

            for nei in adj[node]:
                if nei != prev and not dfs(nei, node): return False

        
            return True
        
        return dfs(0, -1) and len(visited) == n
        
# @lc code=end

