# coding=utf-8
import timeWrapper

@timeWrapper.time_me
def InsertSort(list):
    for i in range(1,len(list)):
        tmp = list[i]
        j=i-1
        while j >=0:
            if ( list[j]>tmp ):
                list[j+1]=list[j]
                list[j]=tmp
            j = j-1
    return list

if __name__=="__main__":
    list = [8,3,6,1,5,0,6,4]
    InsertSort(list)
    print(list)