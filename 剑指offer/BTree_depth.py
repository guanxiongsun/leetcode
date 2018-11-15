# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
1.递归，depth = max(depth_left, depth_right) + 1
2.层序遍历，queue
3.前序、中序、后序

"""
# class Solution:
#     def TreeDepth(self, pRoot):
#         # write code here
#         if pRoot is None:
#             return 0
#         depth_left = self.TreeDepth(pRoot.left)
#         depth_right = self.TreeDepth(pRoot.right)
#         return max(depth_left, depth_right) + 1

# class Solution:
#     def TreeDepth(self, pRoot):
#         # write code here
#         if pRoot is None:
#             return 0
#         queue = [pRoot]
#         max_depth = 0
#         while queue:
#             for i in range(len(queue)):
#                 cur = queue.pop(0)
#                 if cur.left:
#                     queue.append(cur.left)
#                 if cur.right:
#                     queue.append(cur.right)
#             max_depth += 1
#         return max_depth

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        queue = [pRoot]
        max_depth = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            max_depth += 1
        return max_depth
