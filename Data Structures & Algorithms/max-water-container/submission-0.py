class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        max = 0
        
        while (low < high):
            height = min(heights[low], heights[high])
            width = high - low
            water = height * width

            if (water > max):
                max = water
            
            if (heights[low] < heights[high]):
                low += 1
                continue
            
            high -= 1
            
        return max
        