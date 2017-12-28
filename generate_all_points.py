import math


def check_vic(x,y,tx,ty,checked) :
    surr=[(x+1,y),(x-1,y),(x+1,y+1),(x-1,y-1),(x,y+1),(x,y-1)]
    found=False
    while len(surr)!= 0 :
        tempx=surr[0][0]
        tempy=surr[0][1]
        if (tempx,tempy) not in checked :
            checked.append((tempx,tempy))
            if heuristic(tx,ty,tempx,tempy) <= 1 :
                ret=check_vic(tempx,tempy,tx,ty,checked)
                found=ret[0]
                checked=ret[1]
        del surr[0]
    return (found,checked)

def heuristic(x,y,endX,endY) :
    #print endX,endY
    a=math.fabs(x-endX)
    b=math.fabs(y-endY)
    return math.sqrt((a**2+b**2))

print check_vic(0,0,0,0,[])



