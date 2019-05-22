# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # num=[]
        # for mat in matrix:
        #     num+=mat
        # num.sort()
        # return num[k-1]
        return sorted([y for x in matrix for y in x])[k-1]
matrix=[[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
k=8
solution=Solution()
ans=solution.kthSmallest(matrix,k)
print ans