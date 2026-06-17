class Solution:
    def match_strings(self,subs,tab_ref) -> bool:
        tab = {}
        for i in subs:
            if i in tab:
                tab[i] += 1
            else:
                tab[i] = 1
        
        ref = True
        for i in tab_ref:
            ref = ref and i in tab and tab_ref[i] <= tab[i]
        return ref

    def minWindow(self, s: str, t: str) -> str:
        lp=0
        size = len(s)
        out = ""
        rp = len(t) - 1

        tab_ref = {}

        for i in t:
            if i in tab_ref:
                tab_ref[i] += 1
            else:
                tab_ref[i] = 1

        while lp <= rp and rp < len(s):
            subs = s[lp:rp + 1]
            match = self.match_strings(subs,tab_ref)
            if match:
                if len(subs) <= size:
                    size = len(subs)
                    out = subs
                lp += 1
            else:
                rp += 1
        return out

        