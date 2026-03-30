class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total//2

        if len(A) > len(B):
            A, B = B, A

        l = 0
        r = len(A) - 1

        while True:
            am = l + ((r-l)//2) # A
            bm =  half - am - 2# B (half - 1) - (am - 1)

            Aleft = A[am] if am >= 0 else float("-inf")
            Aright = A[am + 1] if (am+1) < len(A) else float("inf")
            Bleft = B[bm] if bm >= 0 else float("-inf")
            Bright = B[bm + 1] if (bm+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total%2:
                    return min(Aright,Bright)
                #even
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft > Bright:
                r = am - 1
            else:
                l = am + 1
