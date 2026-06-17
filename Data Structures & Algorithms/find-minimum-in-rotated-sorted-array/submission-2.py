class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            m = lp + (rp - lp) // 2
            if nums[m] < nums[rp]:
                rp = m
            else:
                lp = m + 1
        return nums[lp]



