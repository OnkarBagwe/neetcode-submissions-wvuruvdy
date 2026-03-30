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
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res