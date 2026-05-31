class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adj = defaultdict(list)
        # tickets.sort()
        # for src,dst in tickets:
        #     adj[src].append(dst)
        #     adj[dst].append(src)
        
        # res = ["JFK"]

        # def dfs(src):
        #     if len(res) == len(tickets) - 1:
        #         return True
            
        #     if src not in adj:
        #         return False
            
        #     temp = list(adj[src])
        #     for i,v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(i)
        #         if dfs(v):
        #             retrun True
        #         adj[src].insert(i,v)
        #         res.pop()
        #     return False

        # dfs("JFK")
        # return res

        adj = defaultdict(list)

        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        res = []
        stack = ["JFK"]

        while stack:
            src = stack[-1]
            if not adj[src]:
                res.append(stack.pop())
            else:
                stack.append(adj[src].pop())

        return res[::-1]