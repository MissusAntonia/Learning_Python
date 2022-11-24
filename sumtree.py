def sumtree(L):
    tot=0
    for x in L:
        if not isinstance(x, list):
            tot+=x
        else:
            tot+=sumtree(x)
    return tot



def sumtree2(L):
    tot=0
    items=list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            print(front,end=' ')
            tot+=front
        else:
            items.extend(front)         # Breath-first <== Append all in nested list
            #items[:0] = front          #  Depth- first <== Prepend all in nested list

    return tot
