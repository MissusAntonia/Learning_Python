'''
• Doesn't support keyword arguments in the tested function call
• Hardcodes the repetitions count
• Charges the cost of range to the tested function’s time
• Always uses time.clock, which might not be best outside Windows
• Doesn't give callers a way to verify that the tested function actually worked
• Only gives total time, which might fluctuate on some heavily loaded machines

'''
import time
def ftimer(func, *arg):
    start=time.perf_counter()
    for i in range(1000):
        func(*arg)
    return time.perf_counter() - start
