class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums = sorted(nums)
        for i in range(0,len(nums)):
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    temp = [nums[i],nums[l],nums[r]]
                    if temp not in out:
                        out.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    r-=1
        return out
