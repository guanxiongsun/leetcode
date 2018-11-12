# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        ans = ''
        for ch in s:
            if ch is ' ':
                ans += '%20'
            else:
                ans += ch
        return ans


# ss = Solution()
# print (ss.replaceSpace("hello word"))