# @before-stub-for-debug-begin
from python3problem210 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = {num: [] for num in range(numCourses)}

        for src, dst in prerequisites:
            adjMap[src].append(dst)

        visited = set()
        processed = set()
        topSort = []

        def dfs(node):  # True = no cycle, False = cycle detected
            if node in visited and node not in processed:
                return False

            if node in visited:
                return True

            visited.add(node)
            for nei in adjMap[node]:
                if not dfs(nei):
                    return False

            processed.add(node)
            topSort.append(node)

            return True

        for node in adjMap:
            if not dfs(node):
                return []

        return topSort


# @lc code=end
