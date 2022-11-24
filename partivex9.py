L= [2, 4, 9, 16, 25]

import math
res1=[]
for i in L:
    res1.append(math.sqrt(i))

res2=list(map(math.sqrt,L))


res3=[math.sqrt(x) for x in L]
res4=list((math.sqrt(x) for x in L))



print(res1,res2,res3,res4)
