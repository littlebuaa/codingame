import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = long(raw_input())
x=[]
y=[]

for i in xrange(N):
    X, Y = [int(i) for i in raw_input().split()]
    x.append(X)
    y.append(Y)

S = float(sum(y))
Moyen =S/len(y)

New = [math.fabs(i-Moyen) for i in y]

index = New.index(min(New))

h=0
for i in y:
    h= h+ int(math.fabs(i-y[index]))

L = max(x)-min(x)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."



print L+h
