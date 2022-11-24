def mysum1(L):
    if not L:
        return 0
    else:
        return L[0] + mysum1(L[1:])

def mysum2(L):
    return 0 if not L else L[0] + mysum2(L[1:])  # Use ternary expression

def mysum3(L):
    return L[0] if len(L) == 1 else L[0] + mysum3(L[1:]) # Any type, assume one

def mysum4(L):
    first, *rest = L
    return first if not rest else first + mysum4(rest) # Use 3.X ext seq assign


def mysum5(L):
    if not L:return 0
    return nonempty(L)

def nonempty(L):
    return L[0] + mysum(L[1:])
        
