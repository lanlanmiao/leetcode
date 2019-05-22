#-*-coding:utf-8 -*-
__author__ = 'guoxuemin'
import re
INT_MAX=2**31-1
INT_MIN=-2**31
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.lstrip()
        if str=='':
            return 0
        flag=1
        if str[0]=='+' and len(str)>1:
            if re.match(r'\d',str[1]):
                new_str=str[1:]
            else:
                return 0
        elif str[0]=='-' and len(str)>1:
            flag=0
            if re.match(r'\d',str[1]):
                new_str=str[1:]
            else:
                return 0
        elif re.match(r'[0-9]',str[0]):
            new_str=str
        else:
            return 0
        num = re.sub("\D", " ", new_str).split(' ')[0]
        num=num.lstrip("0")
        print num
        if flag==1:
            if len(num)>=10 and num>INT_MAX:
                return INT_MAX
            else:
                return int(num)
        else:
            if len(num)>=10 and num>(INT_MAX+1):
                return INT_MIN
            else:
                return -1*int(num)

solution=Solution()
answer=solution.myAtoi("    -00000000023843njnfj")
print answer