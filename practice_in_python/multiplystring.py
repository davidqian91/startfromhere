class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        def leftshift(num, length):
            tail = "0"*length
            return num+tail
        
        if num1 == '0' or num2 == '0':
            return '0'
        l1 = len(num1)
        l2 = len(num2)
        if l1 < l2:
            return self.multiply(num2, num1)
        if l2 <= 5:
            if l1 <= 5:
                n1 = int(num1)
                n2 = int(num2)
                return str(n1*n2)
            else:
                r1 = l1/2
                x = num1[:r1]
                y = num1[r1:]
                high = leftshift(self.multiply(x,num2), len(y))
                low = self.multiply(y,num2)
                return self.plus(high, low)
        else:
            r1 = l1/2
            r2 = l2/2
            x1 = num1[:r1]
            y1 = num1[r1:]
            x2 = num2[:r2]
            y2 = num2[r2:]
            n1 = leftshift(self.multiply(x1,x2), len(y1+y2))
            n2 = leftshift(self.multiply(x1,y2), len(y1))
            n3 = leftshift(self.multiply(x2,y1), len(y2))
            n4 = self.multiply(y1,y2)
            return self.plus(self.plus(n1,n2), self.plus(n3,n4))
            
    def plus(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        if l1 < l2:
            return self.plus(num2, num1)
        c = 0
        res = ""
        for i in range(len(num2)):
            p = int(num2[len(num2)-1-i]) + int(num1[len(num1)-1-i]) + c
            if p >= 10:
                p -= 10
                c = 1
            else:
                c = 0
            res = str(p)+res
        i += 1
        while len(num1)-1-i>=0:
            if c == 0:
                return num1[:len(num1)-i]+res
            p = int(num1[len(num1)-1-i]) + c
            if p >= 10:
                p -= 10
                c = 1
            else:
                c = 0
            res = str(p)+res
            i += 1
        if c == 1:
            return '1'+res
        else:
            return res

s = Solution()
num1 = "658740"
num2 = "668488573"
print(s.multiply(num1, num2))
