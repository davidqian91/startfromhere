class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def isValid(trace, pos):
            if not trace:
                return True
            if pos in trace:
                return False
            l = len(trace)
            for i in range(l):
                if l-i == abs(pos - trace[i]):
                    return False
            return True

        def output(res, n):
            out = []
            for l in res:
                board = []
                for pos in l:
                    s = ""
                    for i in range(n):
                        if i == pos:
                            s += 'Q'
                        else:
                            s += '.'
                    board.append(s)
                out.append(board)
            return out

        res = []
        trace = []
        i = 0
        while True:
            while not isValid(trace, i) and i < n:
                i += 1
            if i == n:
                if trace:
                    i = trace.pop() + 1
                    continue
                else:
                    return output(res, n)
            else:
                trace.append(i)
                if len(trace) == n:
                    res.append(list(trace))
                    i = trace.pop() + 1
                else:
                    i = 0

s = Solution()
print(s.solveNQueens(1))
