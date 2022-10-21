#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

# @lc code=start
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        return self.dfsAndMemo(numCourses, prerequisites, queries)

    def dfsAndMemo(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        @lru_cache(maxsize=None)
        def dfs(node, target):
            if node == target:
                return True

            for nei in adjMap[node]:
                if dfs(nei, target):
                    return True

            return False

        adjMap = {node: [] for node in range(numCourses)}
        for preq, post in prerequisites:
            adjMap[preq].append(post)

        res = []
        for preq, post in queries:
            res.append(dfs(preq, post))

        return res

    def bfsSolution(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        neighbors = {node: set()
                     for node in range(numCourses)}    # store the graph
        indegree = defaultdict(int)     # store indegree info for each node
        # store the prerequisites info for each node
        pre_lookup = defaultdict(set)

        # create the graph
        for pre, post in prerequisites:
            neighbors[pre].add(post)
            indegree[post] += 1

        # add 0 degree nodes into queue for topological sort
        queue = deque([])
        for n in neighbors:
            if indegree[n] == 0:
                queue.append(n)

        # use BFS to do topological sort to create a prerequisite lookup dictionary
        while queue:
            cur = queue.popleft()
            for neighbor in neighbors[cur]:
                # add current node as the prerequisite of this neighbor node
                pre_lookup[neighbor].add(cur)
                # add all the preqs for current node to the neighbor node's preqs
                pre_lookup[neighbor].update(pre_lookup[cur])

                # regular topological search operations
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # traverse the queries and return the results
        result = []
        for preq, post in queries:
            if preq in pre_lookup[post]:
                result.append(True)
            else:
                result.append(False)

        return result
# @lc code=end
