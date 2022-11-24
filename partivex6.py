
def addDict(d1,d2):
    res=d1.copy()
    res.update(d2)
    return res




def addDict2(*args):
    if type(dict()) not in [type(x) for x in args]:
        print('Must be Dictionary')
    else:
        return addDict(*args)


D1={'ola':32,'antu':29}
D2={'a':1,'b':2,'c':3}
L1=[1,2,3,4]
L2=[6,7,8,9]
addDict(D1,D2)
addDict2(D1,D2)
addDict2(L1,L2)
