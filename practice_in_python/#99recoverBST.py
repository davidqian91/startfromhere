##99 recover binary search tree

# to find the two swappd nodes, compare the inorder output of the current tree
# and the sorted result to find the swpped value.
# use binary search to find the node in the tree.
# note that the node we find should have the swapped value.
# since other nodes are not changed, use its original value to
# determine which sub tree to traversal into,
# use swapped val to determine the node


# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
    def binarySearch(self, root, originalVal, swappedVal):
        if root is None:
            return None
        if root.val == swappedVal:
            return root
        elif root.val > originalVal or (root.val == originalVal and 
            originalVal < swappedVal):
            return self.binarySearch(root.left, originalVal, swappedVal)
        else:
            return self.binarySearch(root.right, originalVal, swappedVal)

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
