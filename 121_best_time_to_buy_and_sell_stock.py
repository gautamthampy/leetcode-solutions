from typing import List

# dynamic programming solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)

        return maxP

# 2 pointer approach -> have a buy and sell pointer and move the sell poiter accordingly,
# keeping the buy lower than the selling price and movinf buy to sell if thats not the case
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxP = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                currP = prices[sell] - prices[buy]
                maxP = max(maxP, currP)
            else:    
                buy = sell
            sell += 1

        return maxP        

if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    maxProfit = solution.maxProfit(prices)
    print(maxProfit == 5)       