# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'

'''
冒泡排序对数据操作n-1轮，每轮找出一个最大（小）值。

操作指对相邻两个数比较与交换，每轮会将一个最值交换到数据列首（尾），像冒泡一样。

每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。

额外空间开销出在交换数据时那一个过渡空间，空间复杂度O(1)。
'''
arr=[4,58,3,23,99,23]

def bubbleSort(arr):
    length=len(arr)
    if length<=1:
        return arr
    for i in range(length):
        for j in range(0,length-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print bubbleSort(arr)