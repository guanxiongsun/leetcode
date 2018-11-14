# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
1.递归，depth = max(depth_left, depth_right) + 1
2.非递归

"""

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        depth_left = self.TreeDepth(pRoot.left)
        depth_right = self.TreeDepth(pRoot.right)
        return max(depth_left, depth_right) + 1