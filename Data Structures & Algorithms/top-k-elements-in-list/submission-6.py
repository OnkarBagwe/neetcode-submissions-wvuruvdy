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

        #instead of count = Counter(nums)
        count = {} #instead of count = defaultdict(int)
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        freq = [[] for _ in range(len(nums)+1)]

        for i,c in count.items():
            freq[c].append(i)

        res = []

        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)

            if len(res) == k:
                return res