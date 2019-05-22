# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'

class Solution(object):
    def maxSubArray(self,nums):
        res=nums[0]
        sum=0
        for num in nums:
            if(sum>0):
                sum+=num
            else:
                sum=num
            res=max(res,sum)
        return res

nums=[-2,-1,-3,-4,-1,-2,-1,-5,-4]
solution=Solution()
ans=solution.maxSubArray(nums)
print ans
