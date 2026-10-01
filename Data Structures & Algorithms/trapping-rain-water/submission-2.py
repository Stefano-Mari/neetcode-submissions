class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        left_max = height[0]
        right = len(height) - 1
        right_max = height[-1]
        water = 0

        while left < right:
            
            if height[left] <= height[right]:
                left += 1

                if height[left] > left_max:
                    left_max = height[left]

                water += left_max - height[left]
            
            else:
                right -= 1

                if height[right] > right_max:
                    right_max = height[right]

                water += right_max - height[right]

        return water