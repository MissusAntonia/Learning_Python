print('I am:', __name__)
def lthan(x,y): return x < y
def gthan(x,y): return x > y


def minmax(test,*args):
    res=args[0]
    for arg in args[1:]:
        if test(arg,res):
            res=arg
    return res


if __name__ =='__main__':
    print('Number List: 4,2,1,5,6,3')
    print('Minimum:',minmax(lthan, 4, 2, 1, 5, 6, 3)) # Self-test code
    print('Maximum:',minmax(gthan, 4, 2, 1, 5, 6, 3))
