class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        res = set()
        
        if n1 < n2:
            for n in nums1:
                if n in nums2:
                    res.add(n)
        else:
            for n in nums2:
                if n in nums1:
                    res.add(n)
        
        return list(res)