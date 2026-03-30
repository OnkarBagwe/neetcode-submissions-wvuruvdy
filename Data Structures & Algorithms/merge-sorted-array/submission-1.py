class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last = m + n - 1

        # #merge in reverse order

        # while m > 0 and n > 0:
        #     if nums1[m - 1] > nums2[n - 1]:
        #         nums1[last] = nums1[m - 1]
        #         m -= 1
        #     else:
        #         nums1[last] = nums2[n - 1]
        #         n -= 1
        #     last -= 1

        # #fill leftover elements

        # while n > 0:
        #     nums1[last] = nums2[n - 1]
        #     n -= 1
        #     last -= 1

        #space optimal
        last = m + n - 1
        i, j = m - 1, n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1

            last -= 1