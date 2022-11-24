import sys, os, timeit
defnum, defrep= 1000, 5 # May vary per stmt
def runner(stmts, pythons=None, tracecmd=False):
    print(sys.version)
    for (number, repeat, setup, stmt) in stmts:
        number = number or defnum
        repeat = repeat or defrep
        if not pythons:
            ispy3 = sys.version[0] == '3'
            stmt = stmt.replace('$listif3', 'list' if ispy3 else '')
            best = min(timeit.repeat(setup=setup,stmt=stmt, number=number, repeat=repeat))

        else:
            setup = setup.replace('\t', ' ' * 4)
            setup = ' '.join('-s "%s"' % line for line in setup.split('\n'))
            # Run stmt on all pythons: command line
            # Split lines into quoted arguments
            print('-' * 80)
            print('[%r]' % stmt)
            for (ispy3, python) in pythons:
                stmt1 = stmt.replace('$listif3', 'list' if ispy3 else '')
                stmt1 = stmt1.replace('\t', ' ' * 4)
                lines = stmt1.split('\n')
                args = ' '.join('"%s"' % line for line in lines)
                cmd = '%s -m timeit -n %s -r %s %s %s' % (python, number, repeat,setup,args)
                print(python)
                if tracecmd: print(cmd)
                print('\t' + os.popen(cmd).read().rstrip())
