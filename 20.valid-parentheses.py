#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingMap = {'}': '{', ')': '(', ']' : '[' }
        for char in s:
            if char in closingMap:
                if stack and stack[-1] == closingMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False

        # @lc code=end
