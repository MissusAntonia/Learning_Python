"""
mydir.py: a module that lists the namespaces of other modules
"""
from __future__ import print_function # 2.X compatibility
seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)

    count = 0
    for attr in sorted(module.__dict__): # Scan namespace keys (or enumerate)
        print('%02d) %s' % (count, attr), end = ' ')
        if attr.startswith('__'):
            print('<built-in name>') # Skip __file__, etc.
        else:
            print(getattr(module, attr)) # Same as .__dict__[attr]
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)
if __name__ == '__main__':
    import mydir
    import sys
    if len(sys.argv) == 1:
        listing(mydir)
    else:
        M=sys.argv[1]
        #exec('import '+ M)
        #or
        #__import__(M)
        #or
        import importlib
        importlib.import_module(M)
        Mname=sys.modules[M]
        try:
            N=sys.argv[2]
            N=eval(N)
            listing(Mname,N)
        except:
            listing(Mname)
