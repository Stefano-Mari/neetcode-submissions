class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        if len(s) != len(t): return False

        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        
        for letter in t:
            if counts.get(letter, 0) == 0:
                return False
            counts[letter] -= 1

        return True