# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.out = []
      
    #inorder Traversal
    #do inorder Travelsal to a BST, result should be sorted.
    def inorderTra(self, root):
        if root == None:
            return
        self.inorderTra(root.left)
        self.out.append(root.val)
        self.inorderTra(root.right)
    
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        self.inorderTra(root)
        for i in range(len(self.out)):
            if i==0:
                continue
            if self.out[i]<=self.out[i-1]:
                return False
        return True

S = Solution()
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(6)
e = TreeNode(20)
a.left = b
a.right = c
c.left = d
c.right = e
print(S.isValidBST(a))
