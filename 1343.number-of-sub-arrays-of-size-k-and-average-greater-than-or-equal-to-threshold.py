#
# @lc app=leetcode id=1343 lang=python3
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        average = 0
        count = 0

        for right in range(len(arr)):
            average += arr[right] / k

            if right - left + 1 > k:
                average -= arr[left] / k
                left += 1

            if average >= threshold and right - left + 1 == k:
                count += 1

        return count

# @lc code=end
