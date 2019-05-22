# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'
'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList=s.split(" ")
        for i in range(len(sList)):
            sList[i]=sList[i][::-1]
            #sList[i]=si
        return " ".join(sList)

s="Let's take LeetCode contest"
solution=Solution()
ans=solution.reverseWords(s)
print ans