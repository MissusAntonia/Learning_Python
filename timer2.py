"""
total(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3, b=4)
_reps times, and returns total time for all runs, with final result.

bestof(spam, 1, 2, a=3, b=4, _reps=5) runs best-of-N timer to attempt to
filter out system load variation, and returns best time among _reps tests.

bestoftotal(spam 1, 2, a=3, b=4, _rep1=5, reps=1000) runs best-of-totals
test, which takes the best among _reps1 runs of (the total of _reps runs);

"""


import sys, time
timer=(time.clock if sys.version[0] == '2' else time.perf_counter) if sys.platform[:3] =='win' else time.time

def total(func,*pargs,**kargs):
    """
    Total time to run function(func) (reps)
    amount of time.Returns total time and final result
    """
    _reps=kargs.pop('_reps',1000)
    replist=list(range(_reps))           # Hoist out, equalize 2.x, 3.x
    start=timer()
    for i in replist:
        result=func(*pargs, **kargs)
    elapsed=timer() - start
    return (elapsed,result)

def bestof(func,*pargs,**kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    """
    _reps=kargs.pop('_reps',5)
    #print(pargs,kargs)
    best=2**32
    for i in range(_reps):
        start=timer()
        result=func(*pargs,**kargs)
        elapsed=timer() - start
        if elapsed < best:best=elapsed
    return(best,result)



def bestoftotal(func,*pargs,**kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    _reps1=kargs.pop('_reps1',5)
    return min((total(func,*pargs,**kargs) for i in range(_reps1)))
