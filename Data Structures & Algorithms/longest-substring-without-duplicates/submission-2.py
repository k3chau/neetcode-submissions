class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        hashSet = set()
        left = 0
        right = 0
        while (right < len(s)):
            if s[right] not in hashSet:
                hashSet.add(s[right])
                length = max(length, right - left + 1)
                right = right + 1
            else:
                hashSet.remove(s[left])
                left += 1
        return length


        