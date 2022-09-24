#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openN, closedN, pr):
            if openN == closedN == n:
                res.append(pr)
                return

            if openN < n:
                backtrack(openN + 1, closedN, pr + '(')

            if openN > closedN:
                backtrack(openN, closedN + 1, pr + ')')

        backtrack(0, 0, '')

        return res


# @lc code=end
