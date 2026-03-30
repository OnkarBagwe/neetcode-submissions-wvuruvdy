class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #approach 1 - Min Heap:
        #Time complexity: O(nlogk)
        #Space complexity: O(n+k)
        # h1 = {}
        # res = []
        # for n in nums:
        #     if n in h1:
        #         h1[n] += 1
        #     else:
        #         h1[n] = 1

        # heap = []

        # for key in h1.keys():
        #     heapq.heappush(heap, (h1[key], key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        #approach 2 - Bucket Sort:
        #Time complexity: O(n)
        #Space complexity: O(n)
        count = {}
        res = []
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res