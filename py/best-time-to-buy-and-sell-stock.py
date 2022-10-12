# 121. Best Time to Buy and Sell Stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = prices[0], prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = low
            if prices[i] > high:
                high = prices[i]
                profit = max(high - low, profit)

        return profit


if __name__ == '__main__':
    res = Solution().maxProfit([2, 4, 1])
    print(res)

    res = Solution().maxProfit([2, 4, 1, 2])
    print(res)
