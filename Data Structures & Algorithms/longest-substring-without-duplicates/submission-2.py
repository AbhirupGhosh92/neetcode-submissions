class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tab = set()
        lp=0
        rp=0
        size=0
        temp=0

        while lp <= rp and rp < len(s):
            if s[rp] not in tab:
                temp += 1
                tab.add(s[rp])
                rp += 1
            else:
                size = max(size,temp)
                temp -= 1
                tab.remove(s[lp])
                lp += 1
        return max(size,temp)


        
