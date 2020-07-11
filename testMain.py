# coding=utf-8

import QuickSort
import BubbleSort
import random
import os

if __name__ == "__main__":
    os.system("cls")
    arr = []
    count = int(1e5)
    for i in range(count):
        arr.append(random.random())
    print("开始对各个排序算法进行性能测试，测试用的数据量大小为{}个浮点数".format(count))
    a = arr.copy()
    QuickSort.QuickSort(a)
    a = arr.copy()
    BubbleSort.BubbleSort(a)