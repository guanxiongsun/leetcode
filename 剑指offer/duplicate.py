# -*- coding:utf-8 -*-
"""
    very easy
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        count = [False for _ in numbers]
        for i in numbers:
            if count[i] is True:
                duplication[0] = i
                return True
            else:
                count[i] = True
        return False
