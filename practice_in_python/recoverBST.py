# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.inorder = []

    #inorder Traversal
    #do inorder Travelsal to a BST, result should be sorted.
    def inorderTra(self, root):
        if root is None:
            return
        self.inorderTra(root.left)
        self.inorder.append(root.val)
        self.inorderTra(root.right)

    #binarySearch
    def binarySearch(self, root, target, swappedVal):
        if root is None:
            return None
        if root.val == swappedVal:
            return root
        elif root.val > target or (root.val == target and target < swappedVal):
            return self.binarySearch(root.left, target, swappedVal)
        else:
            return self.binarySearch(root.right, target, swappedVal)

    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.inorderTra(root)
        sVal = 0
        lVal = 0
        sortOrder = sorted(self.inorder)
        for i in range(len(sortOrder)):
            if self.inorder[i] > sortOrder[i]:
                lVal = self.inorder[i]
            elif self.inorder[i] < sortOrder[i]:
                sVal = self.inorder[i]
        s = self.binarySearch(root, sVal, lVal)
        l = self.binarySearch(root, lVal, sVal)
        s.val = sVal
        l.val = lVal
        return root

sol = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
sol.inorderTra(sol.recoverTree(a))
print(sol.inorder)
