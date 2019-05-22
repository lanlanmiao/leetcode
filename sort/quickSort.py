# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'

arr=[4,58,3,23,99,23]

def quickSort(arr,left,right):
    if left<right:
        i,j=left,right
        key=arr[i]
        while i<j:
            while i<j and arr[j]>=key:
                j=j-1
            arr[i]=arr[j]
            while i<j and arr[i]<=key:
                i=i+1
            arr[j]=arr[i]
        arr[i]=key
        quickSort(arr,left,i-1)
        quickSort(arr,j+1,right)
    return arr


print quickSort(arr,0,len(arr)-1)