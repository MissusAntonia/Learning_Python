import timer ,sys
reps=1000
replist=list(range(reps))           # Import timer functions

def forLoop():
    res=[]
    for x in replist:
        res.append(abs(x))
    return res

def listcomp():
    return[abs(x) for x in replist]

def mapcall():
    return list(map(abs,replist))


def genExpr():
    return list((abs(x) for x in replist))

def genFunc():
    def gen():
        for x in replist:
            yield abs(x)
    return list(gen())



print(sys.version)
for test in (forLoop,listcomp,mapcall,genExpr,genFunc):
    (bestof,(total,result))=timer.bestoftotal(5,1000,test)
    print('%-9s:%.5f =>[%s...%s]' %(test.__name__,bestof,result[0],result[-1]) )
