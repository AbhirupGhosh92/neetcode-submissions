class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        # ans = 0
        # for i in range(0,len(heights)):
        #     for j in range(i+1,len(heights)):
        #         length = j-i
        #         height = min(heights[i],heights[j])
        #         area = length * height
        #         ans = max(ans,area)
        # return ans
        lp = 0 
        rp = len(heights) - 1
        ans = 0
        while lp < rp:
            length = rp - lp
            height = min(heights[lp],heights[rp])
            area = length * height
            ans = max(area,ans)
            if heights[lp] < heights[rp]:
                lp += 1
            elif heights[rp] < heights[lp]:
                rp -= 1
            else:
                lp += 1
        return ans


    

