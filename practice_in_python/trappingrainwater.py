class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        st = []
        i = 1
        while i < len(height)-1:
            if height[i] >= height[i+1]:
                i+=1
                continue
            while i < len(height)-1 and height[i+1] > height[i]:
                i+=1
            m = self.findM(height, i)
            if height[m] == 0:
                i+=1
                continue
            while st:
                (l,r) = st[len(st)-1]
                if l >= m:
                    st.pop()
                else:
                    break
            st.append((m,i))
            i+=1
        res = 0
        print(st)
        while st:
            (l,r) = st.pop()
            h = min(height[l],height[r])
            for i in range(l+1, r, 1):
                res += max(h-height[i],0)
        return res

    def findM(self, height, i):
        m = 0
        j = i-1
        while j > 0 and height[j] <= height[j+1]:
            j -= 1
        while j >= 0:
            if height[j] >= height[i]:
                m = j
                break
            elif height[j] > height[m]:
                m = j
            j -= 1
        print(m)
        return m

s = Solution()
height = [0,5,6,4,6,1,0,0,2,7]
print(s.trap(height))
