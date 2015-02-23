from maxDepth_def import *

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.right = d
d.right = e
s = Solution()
print(s.maxDepth(a))