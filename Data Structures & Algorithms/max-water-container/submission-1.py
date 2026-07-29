class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        l = 0
        r = len(height) - 1
        while l < r: 
            width = r - l 
            container_height = min(height[l],height[r])
            currVol = width * container_height
            max_vol = max(max_vol,currVol)
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return max_vol
