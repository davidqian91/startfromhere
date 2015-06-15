class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
         #construct a digram, and run bfs on that until reach the final word
        #BFS
        bfsList = [beginWord]
        toVisit = set(wordDict)
        toDelete = []
        toVisit.delete(beginWord)
        count = 0
        while bfsList:
            u = bfsList.pop(0)
            count += 1
            toDelete = []
            for v in toVisit:
                if self.isAdjacent(u, v):
                    if v == endWord:
                        return count
                    bfsList.append(v)
                    toDelete.append(v)
            for v in toDelete:
                toVisit.delete(v)

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
