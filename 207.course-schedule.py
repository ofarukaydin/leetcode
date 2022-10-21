# @before-stub-for-debug-begin
from python3problem207 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i: [] for i in range(numCourses)}
        visited = set()

        for src, dst in prerequisites:
            adjMap[src].append(dst)

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            for nei in adjMap[node]:
                if not dfs(nei):
                    return False

            visited.remove(node)
            adjMap[node] = []
            return True

        for node in adjMap:
            if not dfs(node):
                return False

        return True

        # @lc code=end
