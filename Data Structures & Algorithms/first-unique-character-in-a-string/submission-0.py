class Solution:
    def firstUniqChar(self, s: str) -> int:
        tab = {}
        for i in range(0,len(s)):
            if s[i] in tab:
                tab[s[i]] += 1
            else:
                tab[s[i]] = 1
        
        for i in range(0,len(s)):
            if s[i] in tab and tab[s[i]] == 1:
                return i
        return -1