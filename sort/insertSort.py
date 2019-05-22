# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'

'''
简单插入排序同样操作n-1轮，每轮将一个未排序树插入排好序列。

开始时默认第一个数有序，将剩余n-1个数逐个插入。插入操作具体包括：比较确定插入位置，数据移位腾出合适空位

每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。

额外空间开销出在数据移位时那一个过渡空间，空间复杂度O(1)。
'''

arr=[4,58,3,23,99,23]

def insertSort(arr):
    n=len(arr)
    if n<=1:
        return arr
    for i in range(1,n):
        j=i
        key=arr[i]
        while j>0 and key<arr[j-1]:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=key
    return arr







print insertSort(arr)