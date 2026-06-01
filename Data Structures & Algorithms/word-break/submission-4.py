class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[n] = True

        for i in range(n-1,-1,-1):
            for w in wordDict:
                if (i+len(w)) <= n and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
        
        return dp[0]

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word):
#         node = self.root
#         for c in word:
#             if c not in node.children:
#                 node.children[c] = TrieNode()
#             node = node.children[c]
#         node.is_word = True
    
#     def search(self,s,i,j):
#         node = self.root
#         for idx in range(i,j+1):
#             if s[idx] not in node.children:
#                 return False
#             node = node.children[s[idx]]
#         return node.is_word

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         trie = Trie()

#         for w in wordDict:
#             trie.insert(w)
        
#         dp = [False] * (len(s) + 1)
#         dp[len(s)] = True

#         t = 0
#         for w in wordDict:
#             t = max(t,len(w))

#         for i in range(len(s),-1,-1):
#             for j in range(i, min(len(s), i + t)):
#                 if trie.search(s,i,j):
#                     dp[i] = dp[j+1]
#                     if dp[i]:
#                         break
        
#         return dp[0]