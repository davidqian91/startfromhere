class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def maxDepth(self, root):
		if root == None:
			return 0
		depth1 = self.maxDepth(root.left)
		depth2 = self.maxDepth(root.right)
		return max(depth1,depth2) + 1