class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n

    def find(self, node):
        p = self.par[node]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.par[n1], self.par[n2]

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailsToAcc = {} # emails -> idx of Acc

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailsToAcc:
                    uf.union(i, emailsToAcc[e])
                else:
                    emailsToAcc[e] = i
        
        emailGroup = defaultdict(list) # idx of acc -> list of emails
        for e, i in emailsToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, e in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i])) # array concat
        
        return res