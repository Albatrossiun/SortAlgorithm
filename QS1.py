def qs(list,left,right):
    if(len(list) == 2) :
        if(list[0]>list[1]):
            list[0],list[1]=list[1],list[0]
            return

    if(left >= right):
        return

    tmp = list[left]
    pleft = left
    pright = right
    while(pleft<pright):
        while(list[pright]>=tmp and pleft<pright):
            pright = pright - 1
        if(pleft==pright):
            break
        list[left] = list[pright]
        while(list[pleft]<=tmp and pleft<pright):
            pleft = pleft + 1
        if(pleft==pright):
            break
        list[pright] = list[pleft]
    list[pleft] = tmp
    qs(list,left,pleft-1)
    qs(list,pleft+1,right)


if __name__=="__main__":
    list = [8,3,6,1,5,0,6,4]
    qs(list,0,7)
    print(list)