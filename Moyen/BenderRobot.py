import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L, C = [int(i) for i in raw_input().split()]
city=[]
start =[]
end = []
door =[]
for i in xrange(L):
    tem =[]
    row = raw_input()
    print >>sys.stderr,row
    for x in row:
        tem.append(x)
        if (x=='@'):
            start.append(i)
            start.append(tem.index(x))
        elif(x=='$'):
            end.append(i)
            end.append(tem.index(x))
        elif(x=='T'):
            door.append([tem.index(x),i])
    city.append(tem)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
#plan =tuple(city)



class robot:
    alive = True
    def __init__(self,x,y,plan,door):
        self.x = x
        self.y = y
        self.p = plan
        self.dir = "SOUTH"
        self.hasBeer = False
        self.inverse = False
        self.door = door
    
    def move(self):
        print >>sys.stderr,"Make decision!!"
        s =[]
        i = 0
        T = False
        while(self.alive):
            y =self.y
            x =self.x
            i+=1
            
            if(i>200):
                T = True
                break
            
            ##########################      Reach the END
            if(self.p[y][x] == '$'):
                self.alive = False
                break
            ##########################      Modifiers of Direction!
            if(self.p[y][x] == 'S'):
                self.dir = "SOUTH"
            if(self.p[y][x] == 'N'):
                self.dir = "NORTH"
            if(self.p[y][x] == 'E'):
                self.dir = "EAST"
            if(self.p[y][x] == 'W'):
                self.dir = "WEST"
            
            ##########################      Drink Beer 
            if(self.p[y][x] == 'B'):
                self.hasBeer = not self.hasBeer
            
            
            ##########################      Inverter of Direction  
            if(self.p[y][x] == 'I'):
                self.inverse = not self.inverse
            
            
            
            ##########################      Telepoters  
            if(self.door):
                if(self.x == self.door[0][0] and self.y == self.door[0][1]):
                    self.x = self.door[1][0]
                    self.y = self.door[1][1]
                    y = self.y
                    x = self.x
                elif(self.x == self.door[1][0] and self.y == self.door[1][1]):
                    self.x = self.door[0][0]
                    self.y = self.door[0][1]
                    y = self.y
                    x = self.x
            ##########################      Movement
            trace = self.avance()
            
            
            s.append(trace)
        
        if(T):
            return ["LOOP"]
        else:
            return s
    
    def avance(self):
        print >>sys.stderr,"Begin to Move!!!"
        y =self.y
        x =self.x
        s =""
        
        if(self.dir == "SOUTH"):
            if(self.p[y+1][x] == '#'):
                self.turn()
                print >>sys.stderr,x,y
                s = self.avance()
            elif(self.p[y+1][x]=='X'):
                if(self.hasBeer):
                    self.p[y+1][x] = ' '
                    self.y +=1
                    s ="SOUTH"
                else:
                    self.turn()
                    print >>sys.stderr,x,y
                    s = self.avance()
            else:
                self.y +=1
                s = "SOUTH"
                print >>sys.stderr,"to South"
                print >>sys.stderr,x,y
               
        elif(self.dir == "EAST"):
            if(self.p[y][x+1]=='#'):
                self.turn()
                print >>sys.stderr,x,y
                s = self.avance()
            elif(self.p[y][x+1]=='X'):
                if(self.hasBeer):
                    self.p[y][x+1] = ' '
                    self.x +=1
                    s = "EAST"
                else:
                    self.turn()
                    s = self.avance()
                    print >>sys.stderr,x,y
            else:
                self.x +=1
                s = "EAST" 
        
        elif(self.dir == "NORTH"):
            if(self.p[y-1][x]=='#'):
                self.turn()
                print >>sys.stderr,x,y
                s = self.avance()
            elif(self.p[y-1][x]=='X'):
                if(self.hasBeer):
                    self.p[y-1][x] =' '
                    self.y -=1
                    s = "NORTH"
                else:
                    self.turn()
                    print >>sys.stderr,x,y
                    s = self.avance()
            else:
                self.y -= 1
                s = "NORTH"
        
        elif(self.dir == "WEST"):
            if(self.p[y][x-1]=='#'):
                self.turn()
                print >>sys.stderr,x,y
                s = self.avance()
            elif(self.p[y][x-1]=='X'):
                if(self.hasBeer):
                    self.p[y][x-1] =' '
                    self.x -=1
                    s = "WEST"
                else:
                    self.turn()
                    print >>sys.stderr,x,y
                    s = self.avance()
            else:
                self.x -=1
                s = "WEST"
        
        return s
            
    def turn(self):
        y =self.y
        x =self.x
        if(not self.inverse):
            if(self.p[y+1][x] != '#' and self.p[y+1][x]!='X'):
                self.dir ="SOUTH"
            elif(self.p[y][x+1]!='#' and self.p[y][x+1]!='X'):
                self.dir = "EAST"
            elif(self.p[y-1][x]!='#' and self.p[y-1][x]!='X'):
                self.dir ="NORTH"
            elif(self.p[y][x-1]!='#' and self.p[y][x-1]!='X'):
                self.dir = "WEST"
        else:
            if(self.p[y][x-1]!='#' and self.p[y][x-1]!='X'):
                self.dir = "WEST"
            elif(self.p[y-1][x]!='#' and self.p[y-1][x]!='X'):
                self.dir ="NORTH"
            elif(self.p[y][x+1]!='#' and self.p[y][x+1]!='X'):
                self.dir = "EAST"
            elif(self.p[y+1][x]!='#' and self.p[y+1][x]!='X'):
                self.dir ="SOUTH"

        
    
y = start[0]   
x = start[1]

print >>sys.stderr,"Starting point:",x,y

print >>sys.stderr,"construct Robot"

r = robot(x,y,city,door)

s = r.move()
print >>sys.stderr,s 


answer = ""
for x in s:
    answer += x + "\n" 

print answer
