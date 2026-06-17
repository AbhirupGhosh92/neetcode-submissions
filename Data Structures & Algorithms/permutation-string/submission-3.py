class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lp = 0
        rp = len(s1) - 1
        tab_init = False
        tab_s1 = {}
        for x in s1:
            if x in tab_s1:
                tab_s1[x] += 1
            else:
                tab_s1[x] = 1
        
        while lp <= rp and rp < len(s2):
            tab_s2 = {}
            subs = s2[lp:rp+1]
            for y in subs:
                if y in tab_s2:
                    tab_s2[y] += 1
                else:
                    tab_s2[y] = 1
            
            res = True
            for p in tab_s1:
                res = res and (p in tab_s2 and tab_s2[p] == tab_s1[p])
            if res:
                return res
            else:
                lp += 1
                rp += 1
        return False
        