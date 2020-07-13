# coding=utf-8
import timeWrapper

def smallHeap(a, b):
    if a < b:
        return True
    return False

def bigHeap(a, b):
    if a > b:
        return True
    return False

class Heap:
    def __init__(self, compareFunc = smallHeap):
        self._c = compareFunc
        self._list = []

    def _AdjustDown(self, index):
        i = index
        list = self._list
        flag = True
        while(flag):
            flag = False
            right = 2 * (i + 1)
            left = right - 1
            tmp = i
            if(right < len(list)):
                if(self._c(list[right], list[tmp])):
                    tmp = right
                    flag = True
            if(left < len(list)):
                if(self._c(list[left], list[tmp])):
                    tmp = left
                    flag = True
            if(flag):
                list[i], list[tmp] = list[tmp], list[i]
                i = tmp

    def BuildHeap(self, list):
        self._list = list.copy()
        for i in range(len(self._list)):
            self._AdjustDown(len(self._list) - 1 - i)  
        
    def _AdjustUp(self, index):
        i = index
        while(True):
            parent = int((i-1)/2)
            if(parent >= 0 and self._c(self._list[i], self._list[parent])):
                self._list[parent], self._list[i] = self._list[i], self._list[parent]
                i = parent
            else:
                break

    def Insert(self, x):
        self._list.append(x)
        self._AdjustUp(len(self._list) - 1)

    def Top(self, x):
        return self._list[0]

    def Pop(self):
        tmp = self._list[0]
        self._list[0] = self._list[len(self._list) - 1]
        self._AdjustDown(0)
        self._list = self._list[0:len(self._list) - 1]
        return tmp

    def Size(self):
        return len(self._list)

    def Empty(self):
        return len(self._list) == 0

    def Show(self):
        print(self._list)

@timeWrapper.time_me
def HeapSort(list):
    h = Heap()
    h.BuildHeap(list)
    tmp = []
    while(not h.Empty()):
        tmp.append(h.Pop())
    list = tmp
    

if __name__ == "__main__":
    h = Heap(bigHeap)
    h.Insert(1)
    h.Insert(3)
    h.Insert(2)
    h.Insert(0)
    h.Insert(5)
    h.Insert(9)
    h.Insert(-1)
    h.Insert(2)
    h.Insert(8)
    h.Show()

    while(not h.Empty()):
        print(h.Pop())