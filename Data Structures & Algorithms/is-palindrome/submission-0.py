class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        pointerA = 0
        pointerB = len(s) - 1
        while pointerA < pointerB:
            if s[pointerA] != s[pointerB]:
                return False
            else:
                pointerA += 1
                pointerB -= 1
        return True

