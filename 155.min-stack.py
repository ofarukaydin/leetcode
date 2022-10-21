# @before-stub-for-debug-begin
from python3problem155 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(self.getMin(), val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else float('inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
