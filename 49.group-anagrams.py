#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = {}
        for str in strs:
            strArray = [0] * 26
            for char in str:
                index = ord(char) - ord('a')
                strArray[index] += 1

            key = tuple(strArray)
            if key in groupedAnagrams:
                groupedAnagrams[key].append(str)
            else:
                groupedAnagrams[key] = [str]

        return groupedAnagrams.values()


# @lc code=end
