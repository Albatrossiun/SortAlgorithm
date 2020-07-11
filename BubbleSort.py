# coding=utf-8

import timeWrapper

@timeWrapper.time_me
def BubbleSort(list):
    size = len(list)
    for i in range(size -1):
        for j in range(size - 1 - i):
            if(list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]