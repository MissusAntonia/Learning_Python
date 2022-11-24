import timer2 ,sys
reps=10000
replist=list(range(reps))

from math import sqrt

def matmod():
    for i in replist:
        res=sqrt(i)
    return res


def powCall():
    for i in replist:
        res=pow(i,.5)
    return res

def powExp():
    for i in replist:
        res=i**.5
    return res



print(sys.version)
for test in (matmod,powCall, powExp):
    (elapsed,result)=timer2.bestoftotal(test, _reps1=3, _reps=1000)
    print ('%s: %.5f => %s' % (test.__name__, elapsed, result))
