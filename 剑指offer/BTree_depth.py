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

# class Solution:
#     def TreeDepth(self, pRoot):
#         # write code here
#         if pRoot is None:
#             return 0
#         depth_left = self.TreeDepth(pRoot.left)
#         depth_right = self.TreeDepth(pRoot.right)
#         return max(depth_left, depth_right) + 1

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        cur = pRoot
        if pRoot is None:
            return 0
        stack = [pRoot]
        times = [1]
        max_depth = 1
        cur_depth = 1
        # while stack:
        #     print stack
        #     while cur.left and times[-1] is not 3:
        #         cur = cur.left
        #         stack.append(cur)
        #         times.append(1)
        #         cur.flag = True
        #         cur_depth += 1
        #         if cur_depth > max_depth:
        #             max_depth = cur_depth
        #     times[-1] += 1
        #     if cur.right and times[-1] is not 3:
        #         cur = cur.right
        #         cur_depth += 1
        #         if cur_depth > max_depth:
        #             max_depth = cur_depth
        #         cur = cur.right
        #         stack.append(cur)
        #         times.append(1)
        #     else:
        #         stack.pop()
        #         times.pop()
        #         times[-1] += 1
        #         cur_depth -= 1
        #         cur = stack[-1]
        while stack:
            while cur and times[-1] != 3:
                stack.append(cur)
                times.append(1)
                cur = cur.left
            if times[-1] == 3:
                stack.pop()
                times.pop()
                cur = stack[-1]
                times[-1] += 1
                if cur.right:
                    cur = cur.right
                    stack.append(cur)
                    times.append(1)
                else:
                    times[-1] += 1
            else:
                cur = stack[-1]
                times[-1] += 1
                if cur.right:
                    cur = cur.right
                    stack.append(cur)
                    times.append(1)
                else:
                    times[-1] += 1
