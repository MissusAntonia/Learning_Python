def f1(a,b):print(a,b)    #Normal Arguments

def f2(a,*b):print(a,b)   #Positional  Variable Arguments

def f3(a,**b):print(a,b)  #keywords variabe Arguments,

def f4(a,*b,**c):print(a,b,c) # Mixed modes

def f5(a,b=2,c=3): print(a,b,c) # keywords arguments

def f6(a,b=2,*c): print(a,b,c) # defaults and positional Arguments
