def rev1(S):
    if len(S) == 1:
        return S
    else:
        return S[-1] + rev1(S[:-1]) # Recursive: 10x slower in CPython today


def rev2(S):
    return ''.join(reversed(S)) # Nonrecursive iterable: simpler, faster


def rev3(S):
    return S[::-1] # Even better?: sequence reversal by slice
