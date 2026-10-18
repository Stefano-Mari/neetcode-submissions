class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            center = (left + right) // 2 

            if nums[center] > nums[right]: # min value can only be after center
                left = center + 1

            else: # min value is or is behind center
                right = center

        return nums[left] # min value has to be the left pointer