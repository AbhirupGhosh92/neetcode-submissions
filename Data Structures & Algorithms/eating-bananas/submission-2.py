class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp = 1
        rp = max(piles)
        result = rp

        while lp <= rp:
            k = lp + (rp - lp) // 2
            hrs = 0
            for i in piles:
                hrs += math.ceil(i/k)
            
            if hrs <= h:
                rp = k - 1
                result = min(result,k)
            else:
                lp = k + 1
        return result


