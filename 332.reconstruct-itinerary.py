# @before-stub-for-debug-begin
from collections import deque
from python3problem332 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjMap = {u: deque() for u, v in tickets}
        res = ['JFK']
        tickets.sort()

        for fromT, toT in tickets:
            adjMap[fromT].append(toT)

        def dfs(curr):
            if len(res) == len(tickets) + 1:
                return True
            if curr not in adjMap:
                return False

            temp = list(adjMap[curr])
            for nei in temp:
                res.append(nei)
                adjMap[curr].popleft()

                if dfs(nei):
                    return True

                res.pop()
                adjMap[curr].append(nei)

            return False

        dfs('JFK')
        return res


# @lc code=end
