def adder(x=1,y=2,z=3):
    return x+y+z



def adder2(**kargs):
    if not kargs:
        return kargs
    else:
        resk=list(kargs.keys())[0]
        resv=kargs.pop(resk)
        for v in kargs.values():
            resv+=v

    return resv



print(adder())
print(adder(5))
print(adder(5, 6))
print(adder(5, 6, 7))
print(adder(x=7, y=6,z=5))
