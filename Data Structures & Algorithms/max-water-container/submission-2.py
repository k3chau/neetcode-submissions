class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        leftptr = 0 
        rightptr = len(heights) - 1
        while leftptr < rightptr:
            width = rightptr - leftptr
            height = min(heights[leftptr], heights[rightptr])
            max_water = max(max_water, width * height)
            if(heights[leftptr] < heights[rightptr]):
                leftptr+= 1
            else:
                rightptr -= 1
        return max_water
        