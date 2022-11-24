from __future__ import print_function # File factorials.py
from functools import reduce
from timeit import repeat
import math          # Import timer functions
import timer ,sys
reps=1000
repslist=list(range(reps))
""" N!, computed as N*(N-1)*(N-2)*...1.
"""

def factrec(N):
    if N == 1:
        return 1
    else:
        return N * factrec(N-1)

def factred(N):
    return reduce((lambda x,y : x*y),range(1,N+1))

def factloop(N):
    count=1
    for i in range(1,N+1):
        count*=i
    return count

def factmod(N):
    return math.factorial(N)



print(sys.version)
for test in (factrec,factred,factloop,factmod):
    (bestof,(total,result))=timer.bestoftotal(5,1000,test,6)
    print('%-9s:%.5f =>[%s]' %(test.__name__,bestof,result) )
print('*'*80)

print(factrec(6), factred(6), factloop(6), factmod(6)) # 6*5*4*3*2*1: all 720
print(factrec(500) == factred(500) == factloop(500) == factmod(500)) # True
for test in (factrec, factred, factloop, factmod):
    print(test.__name__, min(repeat(stmt=lambda: test(500), number=20, repeat=3)))
   
