class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        rp = 0
        size = 0
        tab = {}
        temp = 0
        while lp <= rp and rp < len(s):
            if s[rp] not in tab:
                tab[s[rp]] = 0
                temp += 1 
                rp += 1
            else:
                lp+=1
                rp = lp
                size = max(size,temp)
                temp = 0
                tab = {}
        return max(size,temp)

        
