class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(0, len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)
            if s1 == s2:
                continue
            else:
                heapq.heappush(stones, -abs(s1-s2))
        return -stones[0] if len(stones) == 1 else 0