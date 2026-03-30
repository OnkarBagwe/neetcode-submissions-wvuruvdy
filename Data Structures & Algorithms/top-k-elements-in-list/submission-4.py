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
        count = Counter(nums)
        freq = [[]for i in range(len(nums)+1)]
        res = []

        for i,c in count.items():
            freq[c].append(i)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res