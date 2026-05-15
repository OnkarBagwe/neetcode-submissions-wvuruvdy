class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #TC: O(E*V)
        #But giving TLE on Leetcode
        # adj = {src: [] for src, dst in tickets}
        # tickets.sort()
        # for src, dst in tickets:
        #     adj[src].append(dst)

        # res = ["JFK"]
        # def dfs(src):
        #     if len(res) == len(tickets) + 1:
        #         return True
        #     if src not in adj:
        #         return False

        #     temp = list(adj[src])
        #     for i, v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)
        #         if dfs(v): return True
        #         adj[src].insert(i, v)
        #         res.pop()
        #     return False

        # dfs("JFK")
        # return res

        #Hierholzer's Algorithm
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                res.append(stack.pop())
            else:
                stack.append(adj[curr].pop())

        return res[::-1]