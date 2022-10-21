#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == '+':
                op1 = stack.pop()
                op2 = stack.pop()

                stack.append(op2)
                stack.append(op1)
                stack.append(op1 + op2)
            elif operation == 'D':
                newScore = stack[-1] * 2
                stack.append(newScore)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))

        return sum(stack)

# @lc code=end
