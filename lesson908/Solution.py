# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :param A:
        :param K:
        :return:
        """
        big=max(A)-K
        samll=min(A)+K
        if big>samll:
            return big-samll
        else:
            return 0

solution=Solution()

