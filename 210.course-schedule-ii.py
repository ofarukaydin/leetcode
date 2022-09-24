# @before-stub-for-debug-begin
from collections import deque
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
        adjList = {i: [] for i in range(numCourses)}
        visited = set()

        for course, preq in prerequisites:
            adjList[course].append(preq)

        res = []

        def dfs(node, path):
            if node in path:
                return True

            path.add(node)
            if node not in visited:
                visited.add(node)
                for outgoingNode in adjList[node]:
                    if dfs(outgoingNode, path):
                        return True
                res.append(node)
            path.remove(node)
            return False

        for node in adjList:
            if dfs(node, set()):
                return []

        return res


# @lc code=end


class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        inDegrees = {i: 0 for i in range(numCourses)}

        for course, preq in prerequisites:
            adjList[preq].append(course)
            inDegrees[course] += 1

        zero_indegrees = []

        for node in adjList:
            if inDegrees[node] == 0:
                zero_indegrees.append(node)

        toplogical_sort = []

        while len(zero_indegrees) > 0:
            node = zero_indegrees.pop()
            toplogical_sort.append(node)

            for neighbor in adjList[node]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    zero_indegrees.append(neighbor)

        if len(toplogical_sort) == len(adjList):
            return toplogical_sort
        else:
            return []
