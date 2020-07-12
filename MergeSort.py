def _MergeSort(list,left,right):
    if(left >= right):
        return

    if(right - left == 1):
        if(list[left] > list[right]):
            list[left] , list[right] = list[right] , list[left]
        return
   
    min = int ( ( right - left) / 2 ) + left
    _MergeSort(list,left,min)
    _MergeSort(list,min+1,right)
    tmp = []
    p1 = left
    p2 = min+1
    while( p1 <= min and  p2 <= right):
        if( list[p1]>=list[p2] ):
            tmp.append(list[p2])
            p2 = p2 + 1
        else:
            tmp.append(list[p1])
            p1 = p1 + 1
    while( p1 <= min ):
        tmp.append(list[p1])
        p1 = p1 + 1
    while( p2 <= right):
        tmp.append(list[p2])
        p2 = p2 + 1
    for i in range(len(tmp)):
        list[i + left] = tmp[i]

def MergeSort(list):
    _MergeSort(list,0,len(list)-1)

if __name__=="__main__":
    list = [8,3,6,1,5,0,6,4]
    MergeSort(list)
    print(list)