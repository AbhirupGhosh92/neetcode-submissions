class Solution:

    def index_resolver(self,start,size,idx):
       return (start + idx) % size

    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            m = lp + (rp - lp) // 2
            if nums[m] < nums[rp]:
                rp = m
            else:
                lp = m + 1

        new_lp = 0
        new_rp = len(nums) - 1

        while new_lp <= new_rp:
            new_m = new_lp + (new_rp - new_lp) // 2
            if target < nums[self.index_resolver(lp,len(nums),new_m)]:
                new_rp = new_m - 1
            elif target > nums[self.index_resolver(lp,len(nums),new_m)]:
                new_lp = new_m + 1
            else:
                return self.index_resolver(lp,len(nums),new_m)
        return -1

        
    