#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {c: [] for word in words for c in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))

            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ''

            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
        return self.topsort(graph)

    def topsort(self, graph):
        sortedNodes = []
        visited = {}  # False = visited, True= visited, current path

        def dfs(node):
            # Cycle detected
            if node in visited:
                return visited[node]

            visited[node] = True

            print(f'visited: {node}')
            for nei in graph[node]:
                if dfs(nei):
                    return True

            visited[node] = False

            print(f'added: {node}')
            sortedNodes.append(node)

        for vertex in graph:
            print('Visiting vertex: ', vertex)
            if dfs(vertex):
                return ""

        return ''.join(reversed(sortedNodes))


# @lc code=end
