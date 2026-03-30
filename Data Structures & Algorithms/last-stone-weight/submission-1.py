class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(0, len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s2 > s1:
                heapq.heappush(stones, s1 - s2)
        stones.append(0)
        return abs(stones[0])