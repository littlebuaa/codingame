import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nbFloors: number of floors
# width: width of the area
# nbRounds: maximum number of rounds
# exitFloor: floor on which the exit is found
# exitPos: position of the exit on its floor
# nbTotalClones: number of generated clones
# nbAdditionalElevators: ignore (always zero)
# nbElevators: number of elevators
nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators = [int(i) for i in raw_input().split()]

Lift={}
for i in xrange(nbElevators):
    # elevatorFloor: floor on which this elevator is found
    # elevatorPos: position of the elevator on its floor
    eFloor, ePos = [int(i) for i in raw_input().split()]
    Lift[eFloor]=ePos
# game loop
while 1:
    # cloneFloor: floor of the leading clone
    # clonePos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    cloneFloor, clonePos, direction = raw_input().split()
    cloneFloor = int(cloneFloor)
    clonePos = int(clonePos)

    
    if cloneFloor == -1 and clonePos == -1:
            print "WAIT"
        # Special case (-1,-1)
    else:
        if (cloneFloor != exitFloor):
            if (Lift[cloneFloor] < clonePos) and direction=="RIGHT":
                print "BLOCK"
            elif (Lift[cloneFloor] > clonePos) and direction=="LEFT":
                print "BLOCK"
        # elevitor is either at LEFT or RIGHT of the current clone Pos
        #"BLOCK" it so that the next leader in right direction 
            else:
                print "WAIT"
        elif(cloneFloor == exitFloor):
            if (exitPos > clonePos) and (direction=="LEFT"):
                print "BLOCK"
            elif(exitPos < clonePos) and (direction=="RIGHT"):
                print "BLOCK"
        # Test whether the EXIT is LEFT or RIGHT
        # then choose the right direction by BLOCK the leader
            else:
                print "WAIT"
    
