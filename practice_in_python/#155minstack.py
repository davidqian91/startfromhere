class MinStack:
    def __init__(self):
        self.stack = []
        self.minStk = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if (not self.minStk) or (x <= self.minStk[len(self.minStk)-1]):
            self.minStk.append(x)
        return self.minStk[len(self.minStk)-1]

    # @return nothing
    def pop(self):
        if self.stack[len(self.stack)-1] == self.minStk[len(self.minStk)-1]:
            self.minStk.pop()
        self.stack.pop()

    # @return an integer
    def top(self):
        if not self.stack:
            return NONE
        return self.stack[len(self.stack)-1]

    # @return an integer
    def getMin(self):
        if not self.minStk:
            return NONE
        return self.minStk[len(self.minStk)-1]
        