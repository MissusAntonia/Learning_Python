import pybench, sys


pythons = [
 (1, 'C:\python32\python'),
 (0, 'C:\pypy\pypy-2.0-beta1\pypy')]
stmts = [
# Use function calls: map wins
 (0, 0, "[ord(x) for x in 'spam' * 2500]"),
 (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
 (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
 (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
# Set and dicts
 (0, 0, "{x ** 2 for x in range(1000)}"),
 (0, 0, "s=set()\nfor x in range(1000): s.add(x ** 2)"),
 (0, 0, "{x: x ** 2 for x in range(1000)}"),
 (0, 0, "d={}\nfor x in range(1000): d[x] = x ** 2"),
# Pathological: 300k digits
 (1, 1, "len(str(2**1000000))"), # Pypy loses on this today
 (0, 0, "f=open('randomtext.TXT')\nfor line in f: x=line\nf.close()"),#opening file is also slow in pypy
]
stmts += [
 (0, 0, "def f(x): return x\n[f(x) for x in 'spam' * 2500]"),
 (0, 0, "def f(x): return x\nres=[]\nfor x in 'spam' * 2500: res.append(f(x))"),
 (0, 0, "def f(x): return x\n$listif3(map(f, 'spam' * 2500))"),
 (0, 0, "def f(x): return x\nlist(f(x) for x in 'spam' * 2500)")]

tracecmd = '-t' in sys.argv # -t: trace command lines?
pythons = pythons if '-a' in sys.argv else None # -a: all in list, else one?
pybench.runner(stmts, pythons, tracecmd)
