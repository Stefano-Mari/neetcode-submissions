class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) < len(B):
            A, B = B, A

        l, r = 0, len(B) - 1
        while True:
            i = (l + r) // 2 # B
            j = half - i - 2 # A

            Aleft = A[j] if j >= 0 else float("-inf")
            Aright = A[j + 1] if j + 1 < len(A) else float("inf")
            Bleft = B[i] if i >= 0 else float("-inf")
            Bright = B[i + 1] if i + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    median = (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    median = min(Aright, Bright)
                break

            elif Aleft > Bright:
                l = i + 1
            else:
                r = i - 1

        return median


        
