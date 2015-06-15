class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
         #construct a digram, and run bfs on that until reach the final word
        adj = {}
        for s in wordDict:
            adj[s] = []
            for t in wordDict:
                if self.isAdjacent(s, t):
                    adj[s].append(t)
        #BFS
        bfsList = [beginWord]
        visited = set()
        visited.add(beginWord)
        count = 0
        while bfsList:
            u = bfsList.pop(0)
            count += 1
            for v in adj[u]:
                if v in visited:
                    continue
                if v == endWord:
                    return count
                bfsList.append(v)

    def isAdjacent(self, s, t):
        count = 0
        if s == t:
            return False
        for i in range(s):
            if s[i] != t[i]:
                count += 1
            if count >= 2:
                return False
        return True
