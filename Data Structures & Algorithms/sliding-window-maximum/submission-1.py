class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lp = 0
        rp = k-1
        arr = []
        max_val = -10001
        while rp < len(nums):
            subs = nums[lp:rp + 1]
            if lp == 0:
                max_val = -10001
                for i in subs:
                    max_val = max(i,max_val)
            else:
                if nums[lp-1] == max_val:
                    max_val = -10001
                    for i in subs:
                        max_val = max(i,max_val)
                else:
                    max_val = max(max_val,nums[rp])
            arr.append(max_val)
            lp += 1
            rp += 1
        return arr