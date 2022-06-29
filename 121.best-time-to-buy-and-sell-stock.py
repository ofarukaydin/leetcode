#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPointer, rightPointer = 0, 1
        maxProfit = 0

        while rightPointer < len(prices):
            profit = prices[rightPointer] - prices[leftPointer]

            if profit < 0:
                leftPointer = rightPointer
                rightPointer += 1
            else:
                maxProfit = max(maxProfit, profit)
                rightPointer += 1
        return maxProfit

        
    
            

        
# @lc code=end

