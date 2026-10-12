class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstr = ""
        l = 0
        while l < len(word1) or l < len(word2):
            if l < len(word1):
                newstr += word1[l]
            if l < len(word2):
                newstr += word2[l]
            l += 1
        return newstr 
        