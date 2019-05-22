# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'

'''
简单选择排序同样对数据操作n-1轮，每轮找出一个最大（小）值。

操作指选择，即未排序数逐个比较交换，争夺最值位置，每轮将一个未排序位置上的数交换成已排序数，即每轮选一个最值。

每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。

额外空间开销出在交换数据时那一个过渡空间，空间复杂度O(1)。
'''

arr=[4,58,3,23,99,23]

def selectSort(arr):
    n=len(arr)
    if n<=1:
        return arr
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
           if arr[j]<arr[min]:
               min=j
        if min!=i:
            arr[i],arr[min]=arr[min],arr[i]

    return arr


print selectSort(arr)