class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adj = {src:[] for src,dst in tickets}

        # tickets.sort()

        # for src,dst in tickets:
        #     adj[src].append(dst)

        # res = ["JFK"]

        # def dfs(src):
        #     if len(res) == len(tickets) + 1:
        #         return True
        #     if src not in adj:
        #         return False

        #     temp = list(adj[src])

        #     for i,v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)
        #         if dfs(v):
        #             return True
        #         adj[src].insert(i,v)
        #         res.pop()

        #     return False

        # dfs("JFK")

        # return res

        #Hierholzer's Algorithm
        # adj = defaultdict(list)

        # tickets.sort()

        # for src,dst in tickets[::-1]:
        #     adj[src].append(dst)
        
        # stk = ["JFK"]

        # res = []

        # while stk:
        #     cur = stk[-1]
        #     if not adj[cur]:
        #         res.append(stk.pop())
        #     else:
        #         stk.append(adj[cur].pop())
        # return res[::-1]


        #recursion
        # adj = defaultdict(list)

        # tickets.sort()

        # for src,dst in tickets[::-1]:
        #     adj[src].append(dst)
        
        # res = []

        # def dfs(src):
        #     while adj[src]:
        #         dst = adj[src].pop()
        #         dfs(dst)
        #     res.append(src)
        
        # dfs("JFK")

        # return res[::-1]






        adj = defaultdict(list)

        tickets.sort()
        for src,dst in tickets[::-1]:
            adj[src].append(dst)
        
        stk = ["JFK"]
        res = []

        while stk:
            dst = stk[-1]
            if not adj[dst]:
                res.append(stk.pop())
            else:
                stk.append(adj[dst].pop())
        return res[::-1]
                