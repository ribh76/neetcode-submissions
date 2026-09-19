class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in s:
            i = t.find(char, i)
            if i == -1:
                return False
            i += 1
        
        return True