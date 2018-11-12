# -*- coding:utf-8 -*-
import math
'''
    通过对角线元素判断，左上最小，右下最大
    把方阵分成4份，每份分别判断
    如果有可能在某个块中，则继续划分    
'''


class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array[1]:
            return self.find_in_rect(target, array, 0, 0, len(array))
        return False
    # write code here

    def find_in_rect(self, target, array, x, y, length):
        big = array[x + length - 1][y + length - 1]
        small = array[x][y]
        if target < small or target > big:
            return False
        elif target == small or target == big:
            return True
        else:
            pivot = int(math.floor(float(length)/2))
            length = int(math.ceil(float(length)/2))
            TL = self.find_in_rect(target, array, x, y, length)
            if TL:
                return True
            BR = self.find_in_rect(target, array, x+pivot, y+pivot, length)
            if BR:
                return True
            TR = self.find_in_rect(target, array, x+pivot, y, length)
            if TR:
                return True
            BL = self.find_in_rect(target, array, x, y+pivot, length)
            if BL:
                return True
            return False

# s = Solution()
# print (s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
