def tester(func,items:'tuple',trace=True):
    for i in range(len(items)):
        items=items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))
