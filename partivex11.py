"""
Write a simple recursion function named countdown that prints
numbers as it counts down to zero. For example, a call countdown(5) will print: 5
4 3 2 1 stop. There's no obvious reason to code this with an explicit stack or
queue, but what about a nonfunction approach? Would a generator make sense
here?
"""


def countdown(X):
    while X:
        print(X)
        X-=1
        if X==0:print('stop')

def countdown2(X):
    if not X:
        return 0
    else:
        stack=list(range(X,0,-1))
        if len(stack)== 1:
            print(stack[0])
            print('stop')
        else:
            print(stack[0])
            countdown2(stack[1])

def  countdown3(N):
    if N==0:
        print('stop')
    else:
        print(N)
        countdown3(N-1)


def countdown4(N):
    if N==0:
        yield 'stop'
    else:
        yield N
        for c in countdown4(N-1): yield c
