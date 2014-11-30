# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

n = int(raw_input())
R=[]
for i in xrange(n):
    [X,Y] = [int(x) for x in raw_input().split()]
    R.append([X,Y])	
	
	
def cherche(A,B):
    T = False
    l=[]
    for i in B:
        if (A[1]==i[0]):
            T = True
            l = i
            break
    return [T,l]


N=[]

for i in R:
    num = 2
    T = True
    loo = i
    print >>sys.stderr,loo
    while(T):
        res = cherche(loo,R)
        T= res[0]
        if(T):
            num +=1
            loo = res[1]
    N.append(num)


N.sort(reverse = True)

print >>sys.stderr, N
print N[0]
