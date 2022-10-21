# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        for num in sorted(count):
            while count[num] > 0:
                for i in range(num, num + groupSize):
                    count[i] -= 1
                    if count[i] < 0:
                        return False
        return True

# @lc code=end
