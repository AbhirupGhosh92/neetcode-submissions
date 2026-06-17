class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        lp = 0
        rp = len(s1) - 1
        tab_init = False
        tab_s1 = {}
        tab_s2 = {}
        for x in s1:
            if x in tab_s1:
                tab_s1[x] += 1
            else:
                tab_s1[x] = 1

        for y in range(0,len(s1)):
                if s2[y] in tab_s2:
                    tab_s2[s2[y]] += 1
                else:
                    tab_s2[s2[y]] = 1
        
        while lp <= rp and rp < len(s2):
            res = True
            for p in tab_s1:
                res = res and (p in tab_s2 and tab_s2[p] == tab_s1[p])
            if res:
                return res
            else:
                if s2[lp] in tab_s2:
                    if tab_s2[s2[lp]] > 1:
                        tab_s2[s2[lp]] -= 1
                    else:
                        del tab_s2[s2[lp]]
                else:
                    tab_s2[s2[lp]] = 1
                if rp+1 < len(s2):
                    if s2[rp+1] in tab_s2:
                        tab_s2[s2[rp+1]] += 1
                    else:
                        tab_s2[s2[rp+1]] = 1
            lp += 1
            rp += 1
               
        res = True
        print(tab_s1,tab_s2)
        for p in tab_s1:
            res = res and (p in tab_s2 and tab_s2[p] == tab_s1[p])
        return res
        