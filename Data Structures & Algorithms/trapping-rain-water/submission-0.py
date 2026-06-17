class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = 0
        rmax = 0
        lp = 0
        rp = len(height) - 1
        water = 0
        while (lp < rp):
            lmax = max(height[lp],lmax)
            rmax = max(height[rp],rmax)

            if(lmax < rmax):
                water += lmax - height[lp]
                lp += 1
            elif(lmax > rmax):
                water += rmax - height[rp]
                rp -= 1
            else:
                water += lmax - height[lp]
                lp += 1
        return water

        