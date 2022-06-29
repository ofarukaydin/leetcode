#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = {i: [] for i in range(numCourses)}
        visited = set()

        for crs, preq in prerequisites:
            preqMap[crs].append(preq)

        def dfs(crs):
            if crs in visited:
                return False
            if preqMap[crs] == []:
                return True

            visited.add(crs)

            for preq in preqMap[crs]:
                if not dfs(preq):
                    return False

            visited.remove(crs)
            preqMap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True


# @lc code=end
