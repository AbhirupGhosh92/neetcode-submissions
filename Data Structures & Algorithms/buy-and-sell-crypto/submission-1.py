class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum_val = 0
        lp = 0
        rp = lp + 1
        while lp < rp and rp < len(prices):
            if prices[lp] <=  prices[rp]:
                sum_val = max(sum_val,prices[rp] - prices[lp])
                if prices[rp] <= prices[lp]:
                    lp = rp
                    rp = lp + 1
                else:
                    rp += 1
            else:
                lp += 1
                rp = lp + 1
        return sum_val


