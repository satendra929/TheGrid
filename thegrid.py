from graphics import *
from time import sleep
import math
import random
import copy
import threading
from threading import Thread
from multiprocessing import Process
from heapq import heappush, heappop

status=True

def main() :
    global status
    win= GraphWin("TheGrid", 500, 500)
    win.setBackground('black')
    draw_grid(win)
    #For Fist point
    startX=250
    startY=250
    stpt= Point(startX,startY)
    stcir=Circle(stpt,5)
    stcir.setFill('red')
    stcir.draw(win)
    endX=150
    endY=200
    ept= Point(endX,endY)
    ecir=Circle(ept,5)
    ecir.setFill('blue')
    ecir.draw(win)
    #For Second point
    startX2=450
    startY2=450
    stpt2= Point(startX2,startY2)
    stcir2=Circle(stpt2,5)
    stcir2.setFill('red')
    stcir2.draw(win)
    endX2=250
    endY2=300
    ept2= Point(endX2,endY2)
    ecir2=Circle(ept2,5)
    ecir2.setFill('blue')
    ecir2.draw(win)
    grid=[50,100,150,200,250,300,350,400,450]
    #First point
    pt= Point(startX,startY)
    cir=Circle(pt,5)
    cir.setFill('green')
    cir.draw(win)
    #second point
    pt2= Point(startX2,startY2)
    cir2=Circle(pt2,5)
    cir2.setFill('yellow')
    cir2.draw(win)
    ppoints=pedestrians(win)
    startp=ppoints[0]
    endp=ppoints[1]
    cir_obj=ppoints[2]
    path=find_path(cir,startX,startY,endX,endY,grid)
    path2=find_path(cir2,startX2,startY2,endX2,endY2,grid)
    #Process(target = drive(startX,startY,cir,path)).start()
    Thread(target=drive,args=(startX,startY,cir,path)).start()
    Thread(target=drive,args=(startX2,startY2,cir2,path2)).start()
    Thread(target=move_pedestrians,args=(startp,cir_obj)).start()
    win.getMouse()
    status=False
    win.close()

def drive (startX,startY,cir,path) :
    cX=startX
    cY=startY
    for ind in range (len(path[0])) :
        px=path[0][ind]
        py=path[1][ind]
        cir.move(px-cX,py-cY)
        cX=px
        cY=py
        sleep(0.01)
    return True

def move_pedestrians(startp,cir_obj) :
    while status==True :
        for co in range(len(startp)) :
            positionsx=[startp[co][0]+1,startp[co][0]-1,startp[co][0]]
            positionsy=[startp[co][1]+1,startp[co][1]-1,startp[co][1]]
            ppx=positionsx[random.randint(0,2)]
            ppy=positionsx[random.randint(0,2)]
            cir_obj[co].move(ppx-startp[co][0],ppy-startp[co][0])
            startp[co][0]=ppx
            startp[co][1]=ppy
    return True

def draw_grid(win) :
    l=Line(Point(50,500),Point(50,0))
    l.setFill('green')
    l.draw(win)
    l1=Line(Point(100,500),Point(100,0))
    l1.setFill('green')
    l1.draw(win)
    l2=Line(Point(150,500),Point(150,0))
    l2.setFill('green')
    l2.draw(win)
    l3=Line(Point(200,500),Point(200,0))
    l3.setFill('green')
    l3.draw(win)
    l4=Line(Point(250,500),Point(250,0))
    l4.setFill('green')
    l4.draw(win)
    l5=Line(Point(300,500),Point(300,0))
    l5.setFill('green')
    l5.draw(win)
    l6=Line(Point(350,500),Point(350,0))
    l6.setFill('green')
    l6.draw(win)
    l7=Line(Point(400,500),Point(400,0))
    l7.setFill('green')
    l7.draw(win)
    l8=Line(Point(450,500),Point(450,0))
    l8.setFill('green')
    l8.draw(win)
    lh0=Line(Point(0,0),Point(500,0))
    lh0.setFill('green')
    lh0.draw(win)
    lh=Line(Point(0,50),Point(500,50))
    lh.setFill('green')
    lh.draw(win)
    lh1=Line(Point(0,100),Point(500,100))
    lh1.setFill('green')
    lh1.draw(win)
    lh2=Line(Point(0,150),Point(500,150))
    lh2.setFill('green')
    lh2.draw(win)
    lh3=Line(Point(0,200),Point(500,200))
    lh3.setFill('green')
    lh3.draw(win)
    lh4=Line(Point(0,250),Point(500,250))
    lh4.setFill('green')
    lh4.draw(win)
    lh5=Line(Point(0,300),Point(500,300))
    lh5.setFill('green')
    lh5.draw(win)
    lh6=Line(Point(0,350),Point(500,350))
    lh6.setFill('green')
    lh6.draw(win)
    lh7=Line(Point(0,400),Point(500,400))
    lh7.setFill('green')
    lh7.draw(win)
    lh8=Line(Point(0,450),Point(500,450))
    lh8.setFill('green')
    lh8.draw(win)

def pedestrians(win) :
    spoints=[]
    epoints=[]
    cir_obj=[]
    for i in range(10) :
        spoints.append([random.randint(0,500),random.randint(0,500)])
        epoints.append([random.randint(0,500),random.randint(0,500)])
    for j in spoints :
        pX=j[0]
        pY=j[1]
        ppt= Point(pX,pY)
        pcir=Circle(ppt,2)
        pcir.setFill('white')
        pcir.draw(win)
        cir_obj.append(pcir)
    return (spoints,epoints,cir_obj)
    

def is_path(x,y,grid) :
    for c in grid :
        if x==c :
            return True
        elif y==c :
            return True
    return False

def heuristic(x,y,endX,endY) :
    #print endX,endY
    a=math.fabs(x-endX)
    b=math.fabs(y-endY)
    return math.sqrt((a+b))

def successors(x,y,grid) :
    succ=[]
    if is_path(x+1,y,grid) :
        succ.append((x+1,y))
    if is_path(x,y+1,grid) :
        succ.append((x,y+1))
    if is_path(x-1,y,grid) :
        succ.append((x-1,y))
    if is_path(x,y-1,grid) :
        succ.append((x,y-1))
    return succ

def find_path(cir,startX,startY,endX,endY,grid) :
    fringe=[]
    visited=[]
    cX=startX
    cY=startY
    pathx=[cX]
    pathy=[cY]
    visited.append((cX,cY))
    heu=heuristic(startX,startY,endX,endY)
    heappush(fringe,(heu,(startX,startY,pathx,pathy)))
    while fringe[0]!= IndexError :
        state=heappop(fringe)
        startX=state[1][0]
        startY=state[1][1]
        pX=state[1][2]
        pY=state[1][3]
        if startX==endX and startY==endY :
            return (pX,pY)
        for s in successors(startX,startY,grid) :
            tempX=s[0]
            tempY=s[1]
            temppX=copy.deepcopy(pX)
            temppY=copy.deepcopy(pY)
            if (tempX,tempY) not in visited :
                temppX.append(tempX)
                temppY.append(tempY)
                tempheu=heuristic(tempX,tempY,endX,endY)
                heappush(fringe,(tempheu,(tempX,tempY,temppX,temppY)))
                visited.append((tempX,tempY))

main()
