# -*- coding:utf-8 -*-
"""
    用rear表示滑动框的尾部位置
    从0开始到len(num)-size结束
    1. 首先找到滑动窗内部最大元素max_ele, 和其所在位置 max_ind
    2. 然后滑动过程中判断 a. rear < max_ind and num[head] <= max_ele
                            若成立可以得出此时窗口中最大值为max_ele, 添加到ans中
                       b. num [head] > max_ele
                            若成立 max_ele = num[head], max_ind = head, ans.append(max_ele)
                       c. 若rear超过了max_ind 则用再次更新 max_ele, max_ind = self.findMax(num, rear, size)
    3. 循环直到rear = len(num)-size
"""


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0 or len(num) < size:
            return []
        ans = []
        rear = 0
        # head = rear + size - 1
        max_ele, max_ind = self.findMax(num, rear, size)
        while rear < len(num) - size:
            while rear <= max_ind and rear < len(num) - size:
                head = rear + size - 1
                if num[head] <= max_ele:
                    ans.append(max_ele)
                    rear += 1
                else:
                    ans.append(num[head])
                    max_ind = head
                    max_ele = num[head]
                    rear += 1
            max_ele, max_ind = self.findMax(num, rear, size)
        ans.append(max_ele)
        return ans

    def findMax(self, num, rear, size):
        if rear < 0 or rear + size > len(num):
            return -1, -1
        max_ind = rear
        max_ele = num[rear]
        for ind in range(rear, rear + size):
            if num[ind] > max_ele:
                max_ele = num[ind]
                max_ind = ind
        return max_ele, max_ind


# ss = Solution()
# print (ss.maxInWindows([2,3,4,2,6,2,5,1], 3))
