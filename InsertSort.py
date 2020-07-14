# coding=utf-8
import timeWrapper

def _insert(list, index):
    tmp = list[index]
    ptr = index - 1
    while(ptr >= 0):
        if(list[ptr] > tmp):
            list[ptr + 1] = list[ptr]
            ptr = ptr - 1
        else:
            break
    list[ptr + 1] = tmp

@timeWrapper.time_me
def InsertSort(list):
    if(len(list) <= 1):
        return
    for i in range(len(list) - 1):
        _insert(list, i + 1)


'''def InsertSort(list):
    for i in range(1,len(list)):
        tmp = list[i]
        j=i-1
        while j >=0:
            if ( list[j]>tmp ):
                list[j+1]=list[j]
                list[j]=tmp
            j = j-1
    return list
'''

if __name__=="__main__":
    list = [8,3,6,1,5,0,6,4]
    InsertSort(list)
    print(list)