class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        windowSize = len(s1) 
        l = 0
        r = windowSize 
        while r <= len(s2):
            if sorted(s1) == sorted(s2[l:r]):
                return True
            l += 1
            r += 1
        return False
        

        
            
