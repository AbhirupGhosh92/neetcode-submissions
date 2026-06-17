class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        ans = 0
        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                length = j-i
                height = min(heights[i],heights[j])
                area = length * height
                ans = max(ans,area)
        return ans

    

