class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp = 0
        rp = lp + 1
        size = 0
        while lp < rp and rp < len(s):
            sub_string = s[lp:rp+1]
            tab = {}
            
            for i in sub_string:
                if i in tab:
                    tab[i] += 1
                else:
                    tab[i] = 1
            max_size = 0
            kidx = ""
            for i in tab:
                if tab[i] > max_size:
                    max_size = tab[i]
                    kidx = i
            
            if len(sub_string) - max_size <= k:
                rp += 1
                size = max(size,rp - lp)
            else:
                tab[s[lp]] -= 1
                lp += 1
                if lp == rp:
                    rp += 1
        return size

            
            