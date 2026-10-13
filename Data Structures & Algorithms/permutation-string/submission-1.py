from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)
        r = len(s1)
        l = 0
    

        for _ in range(len(s2)):
            s2_dict = Counter(s2[l:r])

            if s1_dict == s2_dict:
                return True
            r += 1
            l += 1
            
        return False