import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# W: width of the building.
# H: height of the building.
W, H = [int(i) for i in raw_input().split()]
N = int(raw_input()) # maximum number of turns before game over.
X0, Y0 = [int(i) for i in raw_input().split()]


Low = 0
High = H
Left = 0
Right = W

while 1:
   
    BO = raw_input() # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print >>sys.stderr, BO, W, H, N
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    

    if (BO=='U'):
        High= Y0
        Y0=(Low+High)/2
        
    elif(BO == 'D'):
        Low =Y0
        Y0 = (Low +High)/2 
        
    elif(BO == 'L'):
        Right = X0
        X0 = (Left+Right)/2
        
    elif(BO == 'R'):
        Left = X0
        X0 = (Left+Right)/2
        
    elif(BO == 'UR'):
        High= Y0
        Y0= (Low+High)/2
        
        Left = X0
        X0 = (Left+Right)/2

    elif(BO == 'DR'):
        Left = X0
        X0 = (Left+Right)/2
        Low = Y0
        Y0 = (Low +High)/2 
            
    elif(BO == 'DL'):
        Right = X0
        X0 = (Left+Right)/2
        Low =Y0
        Y0 = (Low +High)/2 
  


    elif(BO == 'UL'):
        High= Y0
        Y0= (Low+High)/2
        
        Right = X0
        X0 = (Left+Right)/2
            
    print X0,Y0


