class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index = []
        temp = 0

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums[i+1:]:
                index.append(i)
                index.append(nums.index(temp, i+1))
                print(index)
                return index
            temp = target
            

            

            

        