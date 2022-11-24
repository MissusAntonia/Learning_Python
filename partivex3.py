def adder(*args):
    if not args :
        return args
    else:
        res=args[0]
        for i in args[1:]:
            res+= i
    return res


print(adder([1,2],[3,4]))
print(adder(1,2,3,4))
print(adder(1.2,5.8))
print(adder('ola','antu'))
