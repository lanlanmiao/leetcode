# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'

class Solution(object):
    def maxSubString(self,s):
        res=''
        tmp=''
        k=lambda s1,s2:s1 if len(s1)>len(s2) else s2
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp+=s[i]
            else:
                j=tmp.index(s[i])
                tmp=tmp[j+1:]+s[i]
            if len(res)<len(tmp):
                res=tmp

        return res


s="fhsjhfewiehfdf"
solution=Solution()
ans=solution.maxSubString(s)
print ans