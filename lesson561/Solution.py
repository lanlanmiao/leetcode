# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'

'''
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:

输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
'''
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        nums.sort()
        for i in range(len(nums)):
            if i%2==0:
                res+=nums[i]
        return res

nums=[4,2,3,1]
solution=Solution()
ans=solution.arrayPairSum(nums)
print ans
