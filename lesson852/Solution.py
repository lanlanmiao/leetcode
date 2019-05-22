# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        k=len(A)
        i=0
        j=(k+i)/2
        while j:
            if A[j]>A[j-1] and A[j]>A[j+1]:
                return j
            elif A[j]<A[j-1]:
                k=j
                j=(k+i)/2
            elif A[j]<A[j+1]:
                i=j
                j=(k+i)/2
solution=Solution()
A=[40,48,61,75,100,99,98,39,30,10]
ans=solution.peakIndexInMountainArray(A)
print ans