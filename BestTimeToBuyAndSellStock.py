class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = sys.maxsize
        maxprofit = 0
        
        for price in prices:
            if price < min_so_far:
                min_so_far = price
            else:
                maxprofit = max(price - min_so_far, maxprofit)
        return maxprofit