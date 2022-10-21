# @before-stub-for-debug-begin
from python3problem912 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr

        left = s

        for i in range(s, e):
            if arr[i] < arr[e]:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        arr[e], arr[left] = arr[left], arr[e]

        self.quickSort(arr, s, left-1)
        self.quickSort(arr, left+1, e)

        return arr

    def intertionSort(self, nums):
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                j -= 1

        return nums

    def mergeSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr

        m = (s + e) // 2

        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m+1, e)

        self.merge(arr, s, m, e)

        return arr

    def merge(self, arr, s, m, e):
        l = arr[s:m+1]
        r = arr[m+1:e+1]

        i = 0  # index for l
        j = 0  # index for r
        k = s  # index for arr

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    # @lc code=end
