# -*- coding:utf-8 -*-

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

"""
通过list构建二叉树
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self, list):
        queue = []
        if list:
            self.pRoot = TreeNode(list[0])
            list.pop(0)
            queue.append(self.pRoot)
        else:
            self.pRoot = None
        while list:
            cur = queue.pop(0)
            left = list.pop(0)
            l_node = self.getTnode(left)
            cur.left = l_node
            if l_node:
                queue.append(l_node)
            right = list.pop(0)
            r_node = self.getTnode(right)
            cur.right = r_node
            if r_node:
                queue.append(r_node)

    def getTnode(self, val):
        if val is '#':
            return None
        else:
            return TreeNode(val)


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        stack = [pRoot]
        max_depth = 0

    def isLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

t = Tree([1,2,3,4,'#','#',5,'#',6,7,'#'])
ss = Solution()
ss.TreeDepth(t.pRoot)