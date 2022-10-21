#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        CLOSE_P = [')', ']', '}']
        PARAN_MAP = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        for paran in s:
            if paran not in CLOSE_P:
                stack.append(paran)
            else:
                if stack and PARAN_MAP[stack[-1]] == paran:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
            


# @lc code=end
