class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #approach 1 Hash Table:
        # Time: O(m * n)
        # Space: O(m * n)
        cache = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            cache[tuple(count)].append(s)
        
        return list(cache.values())

        #approach 2 Sorting:
        # Time: O(m * nlogn)
        # Space: O(m * n)
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())