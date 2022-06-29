#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '/', '*']

        for token in tokens:
            if token in operators:
                val2 = stack.pop()
                val1 = stack.pop()
                res = self.evalToken(token, val1, val2)
                stack.append(res)
            stack.append(token)

        return stack[0]

    def evalToken(self, operator, token1, token2):
        if operator == '+':
            return token1 + token2
        elif operator == '-':
            return token1 - token2
        elif operator == '/':
            return token1 // token2
        elif operator == '*':
            return token1 * token2


# @lc code=end
