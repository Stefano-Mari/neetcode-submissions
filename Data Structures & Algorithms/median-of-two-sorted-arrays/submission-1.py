class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        combined = nums1 + nums2
        sort = sorted(combined)
        
        l = 0
        r = len(sort) - 1

        m = (l + r) // 2

        if len(sort) % 2 == 0:
            return (sort[m] + sort[m + 1]) / 2
        else:
            return sort[m]
        