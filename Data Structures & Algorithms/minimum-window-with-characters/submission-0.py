from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        countT = Counter(t)
        need = len(Counter(t))
        have = 0
        best = ""

        if len(t) > len(s): # check if a subtring isn't possible
            return best
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1 # add right character to window count

            if c in countT and window[c] == countT[c]: # check if right character is in t and the counts match
                have += 1
            
            while need == have:
                if best == "" or r - l + 1 < len(best): # get new best
                    best = s[l:r + 1]
                
                window[s[l]] -= 1 # decrement character count at left
                if s[l] in countT and window[s[l]] < countT[s[l]]: # check if left char in t and counts don't match
                    have -= 1
                l += 1

        return best     