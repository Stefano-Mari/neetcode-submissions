class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index = []

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i == j:
                    continue

                if (nums[i] + nums[j] == target):
                    index.append(i)
                    index.append(j)
                    return index