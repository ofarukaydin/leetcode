#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed))[::-1]


        for pos, speed in pairs:
            dist = target - pos
            arrivalTime = dist / speed

            if not stack:
                stack.append(arrivalTime)
            elif arrivalTime > stack[-1]:
                stack.append(arrivalTime)

        return len(stack)
# @lc code=end
