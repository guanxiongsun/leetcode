# -*- coding:utf-8 -*-
"""
medium
第一种解法用了除法
第二种解法将表达式从i位置分开，
    第一次遍历计算B[i]表达式中前面部分（A[0~i-1]）的乘机，
        此时可以通过B[i+1] = B[i]*A[i+1]得到
    第二次从后向前遍历B数组，此时需要做的是在B[i]的基础上乘以A[i+1~n-1]的乘积，
        此时可以通过 tmp表示该乘积,有 tmp = tmp*A[i+1]
            所以 B[i-1] = B[i]*tmp
"""


# class Solution:
#     def multiply(self, A):
#         # write code here
#         length = len(A)
#         multiple = 1
#         for ind in range(length):
#             if A[ind] is not 0:
#                 multiple *= A[ind]
#             else:
#                 for a in A[ind + 1:]:
#                     multiple *= a
#                 B = [0]*length
#                 B[ind] = multiple
#                 return B
#         for ind in range(length-1, 0, -1):
#             if A[ind] is not 0:
#                 A[ind] = float(A[ind-1])/float(A[ind])
#         A[0] = 1/float(A[0])
#         B = [None]*length
#         B[0] = multiple*A[0]
#         for ind in range(1, length):
#             B[ind] = int(B[ind-1]*A[ind])
#         return B


class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        # 第一遍，计算表达式中A[0~i-1]部分
        B = [None]*length
        B[0] = 1
        for ind in range(1, length):
            B[ind] = B[ind-1]*A[ind-1]

        # 第二遍，计算表达式中A[n-1~i+1]部分，并乘以B[i]
        tmp = 1
        for ind in range(length-2, -1, -1):
            tmp *= A[ind+1]
            B[ind] *= tmp
        return B


# ss = Solution()
# print (ss.multiply ([1,2,3,4,5]))