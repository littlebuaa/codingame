import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in raw_input().split()]

Link =[]
for i in xrange(L):
    # N1: N1 and N2 defines a link between these nodes
    N1, N2 = [int(i) for i in raw_input().split()]
   
    Link.append([N1,N2])


Exit =[]
for i in xrange(E):
    EI = int(raw_input()) # the index of a gateway node
    Exit.append(EI)
# game loop

for i in Link:
    for j in Exit:
        if (i[1]== j):
            i[1]=i[0]
            i[0]=j


while 1:
    SI = int(raw_input()) # The index of the node on which the Skynet agent is positioned this turn
    print >> sys.stderr,SI
    
    nearE = False
    print >>sys.stderr,Link
    for i in Link:
        loop = False
        
        for j in Exit:
            if((SI==i[1]) and (j==i[0])):
                print i[1], i[0]
                i[1] =-1
                nearE = True
                loop = True
                break
        if(loop):
            break
        
    if(not nearE):
        print >>sys.stderr,"Not danger"
        for i in Link:
            loop = False
            for j in Exit:
                if((j==i[0])and (i[1]>0)):
                    print i[1],j
                    i[0]=-1
                    loop = True
                    break
            if(loop):
                break
            
    
    
    
