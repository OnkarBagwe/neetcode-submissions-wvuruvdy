class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)

        for i in range(len(edges)):
            u,v = edges[i]
            adj[u].append([v, succProb[i]])
            adj[v].append([u, succProb[i]])

        visit = set()
        pq = [(-1, start)]

        while pq:
            prob, node = heapq.heappop(pq)
            visit.add(node)

            if node == end:
                return prob * -1
            
            for nei, edgeProb in adj[node]:
                if nei not in visit:
                    heapq.heappush(pq, (edgeProb*prob, nei))

        return 0