class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            m = lp + ((rp-lp)//2)
            if nums[m] > target:
                rp = m - 1
            elif nums[m] < target:
                lp = m + 1
            else:
                return m
        return -1
                

         