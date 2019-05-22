# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        max=len(nums)-1
        min=0
        while min<max:
            mid=(min+max)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                max=mid
            else:
                min=mid
        return -1


nums=[-1,0,3,5,9,12]
target=5
solution=Solution()
ans=solution.search(nums,target)
print ans
