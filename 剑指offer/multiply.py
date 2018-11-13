# -*- coding:utf-8 -*-
"""
    easy
"""


class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        multiple = 1
        for ind in range(length):
            if A[ind] is not 0:
                multiple *= A[ind]
            else:
                for a in A[ind + 1:]:
                    multiple *= a
                B = [0]*length
                B[ind] = multiple
                return B
        for ind in range(length-1, 0, -1):
            if A[ind] is not 0:
                A[ind] = float(A[ind-1])/float(A[ind])
        A[0] = 1/float(A[0])
        B = [None]*length
        B[0] = multiple*A[0]
        for ind in range(1, length):
            B[ind] = int(B[ind-1]*A[ind])
        return B

# ss = Solution()
# print (ss.multiply ([1,2,3,4,5]))