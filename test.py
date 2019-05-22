#-*-coding:utf-8 -*-
__author__ = 'guoxuemin'

s1='wjekjew'
s2='fjkwjekwjekwje'
func=lambda s1,s2:s1 if len(s1)>len(s2) else s2

print func(s1,s2)
ll=[1,2,3,4]
print ll[::-1]