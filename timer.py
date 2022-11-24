"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time

"""


import sys, time
timer=(time.clock if sys.version[0] == '2' else time.perf_counter) if sys.platform[:3] =='win' else time.time


def total(reps,func,*pargs,**kargs) :
    """
    Total time to run function(func) (reps)
    amount of time.Returns total time and final result
    """
    replist=list(range(reps))           # Hoist out, equalize 2.x, 3.x
    start=timer()
    for i in replist:
        result=func(*pargs, **kargs)
    elapsed=timer() - start
    return (elapsed,result)


def bestof(reps,func,*pargs,**kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    """
    #print(pargs,kargs)
    best=2**32
    for i in range(reps):
        start=timer()
        result=func(*pargs,**kargs)
        elapsed=timer() - start
        if elapsed < best:best=elapsed
    return(best,result)



def bestoftotal(reps1,reps2,func,*pargs,**kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1,total,reps2,func,*pargs,**kargs)
