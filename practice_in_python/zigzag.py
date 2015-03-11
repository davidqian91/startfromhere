#Given a binary tree, return the zigzag level order traversal of its nodes' values. 
#(ie, from left to right, then right to left for the next level and alternate between).
#
#use two stacks, one stack contain the node that is outputing,
#and add its child elements to the other,
#so in the layer that we output from left to right ,
#add the left child to the other stack first,
#vice versa


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        s1 = []
        s2 = []
        re = []
        b = True
        s1.append(root)
        while(s1 or s2):
            if b:
                line = []
                while(s1):
                    n = s1.pop()
                    line.append(n.val)
                    if n.left:
                        s2.append(n.left)
                    if n.right:
                        s2.append(n.right)
                re.append(line)
                b = not b
            else:
                line = []
                while(s2):
                    n = s2.pop()
                    line.append(n.val)
                    if n.right:
                        s1.append(n.right)
                    if n.left:
                        s1.append(n.left)
                re.append(line)
                b = not b
        return re
