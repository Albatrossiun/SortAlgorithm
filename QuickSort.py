# coding=utf-8
# 上边一行是用来告诉python解释器，这个文件的编码格式
import timeWrapper

def _miniSort(list, left, right):
    if(list[left] > list[right]):
        list[left], list[right] = list[right], list[left]
    return 

def _quickSort(list, left, right):
    if(left >= right):
        return
    if(right - left == 1):
        _miniSort(list, left, right)
        return
    tmp = list[left]
    pleft = left
    pright = right
    while(pleft < pright):
        while(list[pright] > tmp and pright > pleft):
            pright = pright - 1
        if(pright == pleft):
            break
        list[pleft] = list[pright]
        while(list[pleft] <= tmp and pleft < pright):
            pleft = pleft + 1
        if(pleft == pright):
            break
        list[pright] = list[pleft]
    list[pleft] = tmp
    _quickSort(list, left, pleft - 1)
    _quickSort(list, pright + 1, right)

@timeWrapper.time_me
def QuickSort(list):
    _quickSort(list, 0, len(list) - 1)

