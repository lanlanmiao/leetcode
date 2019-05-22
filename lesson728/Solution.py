# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        if right<10:
            return range(left,right+1)
        res=[]
        for i in range(left,right+1):
            s=str(i)
            flag=True
            for num in s:
                if not int(num) or i%int(num)!=0:
                    flag=False
                    break
            if flag:
                res.append(i)
        return res



solution=Solution()
ans=solution.selfDividingNumbers(1,10000)
print ans