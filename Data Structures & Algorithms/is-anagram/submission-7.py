class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMaps = {}
        hashMapt = {}
        for char in s: 
            if char not in hashMaps:
                hashMaps[char] = 1
            else:
                hashMaps[char] += 1
        for char in t: 
            if char not in hashMapt:
                hashMapt[char] = 1
            else:
                hashMapt[char] += 1
        return hashMaps == hashMapt

    
        