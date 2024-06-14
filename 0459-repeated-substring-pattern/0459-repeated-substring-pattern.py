class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        if len(s) < 2:
            return False
        
        new_s = (s + s)[1:-1]
        
        return s in new_s

        