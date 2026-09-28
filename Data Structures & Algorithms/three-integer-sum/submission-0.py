class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0: # impossible combination
                break 
            
            elif i > 0 and nums[i] == nums[i - 1]: # skip duplicate anchors
                continue

            low = i + 1
            high = len(nums) - 1

            while (low < high):
                s = nums[i] + nums[low] + nums[high]

                if s == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]: # skip duplicate lows
                        low += 1
                elif s > 0:
                    high -= 1
                else:
                    low += 1
        return res    
        