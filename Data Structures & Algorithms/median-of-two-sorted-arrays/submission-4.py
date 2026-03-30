class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l = 0
        r = len(A) - 1

        while True:
            i = l + (r-l)//2
            j = half - i - 2
            
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i < len(A) - 1 else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j < len(B) - 1 else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1