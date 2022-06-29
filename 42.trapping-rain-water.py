#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWaters = 0
        left = 0

        while left < len(height) - 1:
            if height[left] == 0:
                left += 1
                continue

            right = left + 1
            currentTrappedWaters = 0

            while (
                right < len(height) and
                height[right] < height[left]
            ):
                diff = height[left] - height[right]
                currentTrappedWaters += diff
                right += 1

            if right < len(height):
                trappedWaters += currentTrappedWaters
                left = right
                continue
            else:
                reversedList = list(reversed(height[left:right]))
                return trappedWaters + self.trap(reversedList)

        return trappedWaters


# @lc code=end
