class Solution:
    # @param {character[][]} board
    # @return {boolean}
    
    def __init__(self):
        self.candidates = []
        self.trace = []

    def solveSudoku(self, board):
        self.calc_candidate(board)
        status = False
        while not self.isFinish(board):
            if status:
                status = False
            else:
                (i, j, num, b) = self.find_a_candidate(board)
            board[i][j] = num
            self.trace.append((i, j, num, b))
            if not self.candidate_change(i, j, board):
                while b and self.trace:
                    (i, j, num, b) = self.trace.pop()
                    board[i][j] = '.'
                self.calc_candidate(board)
                index = self.candidates[i][j].index(num)
                index += 1
                num = self.candidates[i][j][index]
                b = index == (len(self.candidates[i][j])-1)
                status = True

    def isFinish(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return False
        return True

    def calc_candidate(self, board):
        self.candidates = [[['1','2','3','4','5','6','7','8','9'] for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    for p in range(9):
                        if board[i][j] in self.candidates[p][j]:
                            self.candidates[p][j].remove(board[i][j])
                        if board[i][j] in self.candidates[i][p]:
                            self.candidates[i][p].remove(board[i][j])
                    if i == 3 and j == 6:
                        pass
                    for m in range(i-i%3, i-i%3+3, 1):
                        for n in range(j-j%3, j-j%3+3, 1):
                            if board[i][j] in self.candidates[m][n]:
                                self.candidates[m][n].remove(board[i][j])

    def candidate_change(self, i, j, board):
        for p in range(9):
            if board[i][j] in self.candidates[p][j]:
                self.candidates[p][j].remove(board[i][j])
                if board[p][j] == '.' and not self.candidates[p][j]:
                    return False
            if board[i][j] in self.candidates[i][p]:
                self.candidates[i][p].remove(board[i][j])
                if board[i][p] == '.' and not self.candidates[i][p]:
                    return False
        for m in range(i-i%3, i-i%3+3, 1):
            for n in range(j-j%3, j-j%3+3, 1):
                if board[i][j] in self.candidates[m][n]:
                    self.candidates[m][n].remove(board[i][j])
                    if board[m][n] == '.' and not self.candidates[m][n]:
                        return False
        return True

    def find_a_candidate(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.' and len(self.candidates[i][j]) == 1:
                    return (i, j, self.candidates[i][j][0], True)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.' and len(self.candidates[i][j]) > 1:
                    return (i, j, self.candidates[i][j][0], False)
        return None

s = Solution()
data = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = [[]for row in range(9)]
for i in range(9):
    for j in range(9):
        board[i].append(data[i][j])
s.solveSudoku(board)
