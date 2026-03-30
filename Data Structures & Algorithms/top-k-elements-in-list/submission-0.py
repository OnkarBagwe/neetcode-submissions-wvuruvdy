class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h1 = {}
        res = []
        for n in nums:
            if n in h1:
                h1[n] += 1
            else:
                h1[n] = 1

        heap = []

        for key in h1.keys():
            heapq.heappush(heap, (h1[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res