import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(raw_input())
L = int(raw_input())

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

def Con(A):
    num = []        # list to return 
    count =1        # counter of the consecutive same number
    A.append(-1)    # add one number at last for counting
    for i in xrange(len(A)-1):
        if (A[i]==A[i+1]):
            count +=1   # same number, count
        else :
            num.append(count)   # Add frequency
            num.append(A[i])    # Add number
            count =1            # Reset count
    return num


# Loop     

seed =[R]
for i in xrange(L-1):
    seed = Con(seed)
# Output
answer = ""    
for i in xrange(len(seed)):
    answer += str(seed[i])+" "
    
answer = answer.rstrip()    # Remove the last SPACE  

print answer
